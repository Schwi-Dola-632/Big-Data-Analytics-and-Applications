# LongMemEval 数据集还原

为满足 GitHub 普通文件大小限制，两个较大的 JSON 文件采用无损 gzip 压缩；超过 90 MiB 的压缩文件按顺序分卷。其余原始文件保持原样。

下载本目录的所有文件后，使用 Python 3.8 或更新版本执行：

```powershell
python restore.py
```

脚本会在本目录还原原始 JSON，并根据 `manifest.json` 验证每个原始文件的大小和 SHA-256。无需安装第三方依赖。已有的原始文件仅校验，不覆盖。请为还原后的数据预留至少 3.1 GB 空间。

`README.md` 和 `gitattributes.txt` 来自原始下载目录。`gitattributes.txt` 保留为数据来源附带文件，并非本仓库的 Git 属性配置。
