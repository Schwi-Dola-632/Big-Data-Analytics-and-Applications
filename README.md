# Big-Data-Analytics-and-Applications
ScopeDrift educational pilot package
Version 2026-10-30

Read the accompanying Chinese Word manual before the real experiment.
This package is an author-created pilot harness, not the official LongMemEval or LoCoMo implementation.
It contains NO downloaded dataset, API key, real model response or experimental result.
Offline checks used mocked responses only; no live-provider compatibility claim is made.

Files
  requirements.txt     plot dependencies; API uses Python standard library
  data.py              inspect official JSON and extract unchanged background sessions
  make_case.py         create one synthetic-rule template / merge reviewed case arrays
  experiment.py        validate, run, export, repair, export-repair
  plot_results.py      generate 300 dpi PNG and SVG from completed human labels

Quick start (Windows PowerShell in extracted folder)
  py -3 -m venv .venv
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
  .\.venv\Scripts\python.exe make_case.py --demo --out demo_cases.json
  .\.venv\Scripts\python.exe experiment.py validate --cases demo_cases.json

Set MODEL_BASE_URL (without /chat/completions), WRITER_MODEL, READER_MODEL,
and MODEL_API_KEY in your terminal using the provider's official console.
A paid run starts only when YOU execute run or repair. Default call cap is 20.
No automatic network retries: inspect failures before resuming.
The cap resets per command invocation, and is not a monetary budget limit.

Run demo
  .\.venv\Scripts\python.exe experiment.py run --cases demo_cases.json --out runs/demo --max-calls 20
Repeat the SAME command to resume. One case x one repetition x three methods
uses 58 calls, produces 18 snapshots and 54 behavior label rows.
  .\.venv\Scripts\python.exe experiment.py export --cases demo_cases.json --out runs/demo
Fill memory_labels.csv and behavior_labels.csv. See Word manual for labels.
  .\.venv\Scripts\python.exe plot_results.py runs/demo

Repair
Copy repairs_template.json to repairs.json, retain ALL pre-specified eligible
round-5 recursive scope-drift snapshots, and fill repair, sham, reason.
  .\.venv\Scripts\python.exe experiment.py repair --cases demo_cases.json --out runs/demo --max-calls 20
  .\.venv\Scripts\python.exe experiment.py export-repair --cases demo_cases.json --out runs/demo
Fill repair_labels.csv and rerun plot_results.py. For runs with --repeats 3
or --mode pure, repeat those arguments in run and repair commands.

Limits
Freeze is a diagnostic M0-only condition, not a matched-capacity practical system.
Output 200-word instruction + 768-token hard limit is not exact token matching.
Reader outputs and memory labels require manual review. Unknown labels must be
reported. Plots bootstrap semantic families conditional on selected backgrounds;
shared source conversations and finite LoCoMo backgrounds limit generalization.
Do not pool demo, development, held-out test, stream or pure runs.
No benchmark-original QA, BM25, training or auto scope repair implemented.
Data and code rights for official datasets remain with original publishers.
