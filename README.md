# UC03 Static Triage – Real Pull Request Demo

Purpose-built repository to demonstrate **UC03** in the SE373 Desktop Workbench with a real GitHub pull request. The `main` branch is clean. The `demo/uc03-static-defects` branch intentionally introduces two static-analysis-relevant security issues and two logical defects. The defects are **intentional educational fixtures**, not claims that UC03 will automatically detect every one.

## Review scenario

A proposed change to order processing requires security and correctness review. Run UC03 static triage, inspect the analyzer evidence, and compare findings to independent reviewer labels.

## Create a real GitHub PR

1. Install Git, GitHub CLI (`gh`) and authenticate with `gh auth login`.
2. Run `powershell -ExecutionPolicy Bypass -File .\publish-demo.ps1` from this directory.
3. Copy the printed PR URL and import it into Desktop Workbench.
4. Choose `UC03 · Static Triage` in Settings, verify Docker/analysers and provider, then start review.
5. Inspect `static-analysis.jsonl`, `diagnostic-decisions.jsonl`, `static-finding-links.jsonl`, `report.json`, `validation.json`, `trace.jsonl` in the run directory.

Use a new repo with no sensitive data. Do not put the ground-truth list into the model prompt when testing blind quality. Ground truth is in `OPERATOR_ONLY_GROUND_TRUTH.txt`, excluded from Git by `.gitignore`. Keep it outside the Agent workspace.
