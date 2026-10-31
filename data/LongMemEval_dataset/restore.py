"""Restore losslessly compressed JSON files and verify all source files."""
from pathlib import Path
import gzip
import hashlib
import io
import json


class PartsReader(io.RawIOBase):
    def __init__(self, paths):
        self.paths = iter(paths)
        self.current = None

    def readable(self):
        return True

    def readinto(self, target):
        while True:
            if self.current is None:
                path = next(self.paths, None)
                if path is None:
                    return 0
                self.current = path.open('rb')
            n = self.current.readinto(target)
            if n:
                return n
            self.current.close()
            self.current = None

    def close(self):
        if self.current is not None:
            self.current.close()
        super().close()


def main():
    root = Path(__file__).resolve().parent
    records = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    for record in records:
        output = root / record['file']
        compressed = record['stored'] != [record['file']]
        digest = hashlib.sha256()
        size = 0
        if compressed and not output.exists():
            temp = output.with_name(output.name + '.restoring')
            try:
                with PartsReader([root / p for p in record['stored']]) as parts:
                    with io.BufferedReader(parts) as buffered, gzip.GzipFile(fileobj=buffered) as source:
                        with temp.open('xb') as target:
                            for chunk in iter(lambda: source.read(8 * 1024**2), b''):
                                digest.update(chunk)
                                size += len(chunk)
                                target.write(chunk)
                if digest.hexdigest() != record['sha256'] or size != record['size']:
                    raise ValueError('Verification failed: ' + record['file'])
                temp.rename(output)
            except BaseException:
                temp.unlink(missing_ok=True)
                raise
        else:
            with output.open('rb') as source:
                for chunk in iter(lambda: source.read(8 * 1024**2), b''):
                    digest.update(chunk)
                    size += len(chunk)
            if digest.hexdigest() != record['sha256'] or size != record['size']:
                raise ValueError('Verification failed: ' + record['file'])
        print('Verified:', record['file'])


if __name__ == '__main__':
    main()
