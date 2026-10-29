---
license: mit
task_categories:
- other
tags:
- safety
- prompt-injection
- agent-safety
- benchmark
- adversarial
- llm-agent
size_categories:
- n<1K
configs:
- config_name: cases
  data_files: data/cases.jsonl
---

# ClawSafety — Case Catalog (HF-ready metadata view)

Structured, HF-viewer-friendly catalog of the **ClawSafety** benchmark cases (arXiv 2604.01438): *"ClawSafety: Safe LLMs, Unsafe Agents"* — a safety benchmark for personal AI agents under realistic indirect prompt injection (120 adversarial cases across 5 professional domains, 3 injection vectors, 5 harmful action types).

## ⚠️ Scope of this dataset: metadata only

This HF dataset contains the **case catalog** (ids, harmful-action types, attack vectors, flags) — **it does not contain adversarial payloads**. Working payloads (including honey tokens) stay in the [GitHub repository](https://github.com/weibowen555/ClawSafety), as required by its [SECURITY.md](https://github.com/weibowen555/ClawSafety/blob/main/SECURITY.md). This keeps the dataset safe to browse for discovery/citation while payload access follows the upstream responsible-use policy.

## Current coverage (v0.1.0 release)

Scenario **S2 (Financial Operations — "Quarter-End Settlement Night")**, 17 cases:

| Attack vector | Cases |
|---|---|
| skill (SKILL.md) | 8 |
| email | 7 |
| meeting_notes (planted document) | 1 |
| planted_file (wallet history) | 1 |

| Harmful action type | Cases |
|---|---|
| config_exfil | 8 |
| destination_substitution | 3 |
| config_modification | 2 |
| credential_forwarding | 2 |
| file_move | 1 |
| unauthorized_action | 1 |

S1/S3/S4/S5 scenarios and the web-injection cases are pending the upstream v0.2.0 release.

## Fields

- `case_id` — e.g. `FL-A1`
- `scenario` — benchmark scenario (`S2_financial`)
- `harmful_action_type` — one of the paper taxonomy types
- `attack_vector` — `skill` / `email` / `meeting_notes` / `planted_file` (inferred from case metadata; `web` will appear once upstream web cases are released)
- `name` — human-readable case description
- `flags` — case toggles (e.g. `uses_injected_meeting_notes`, `poison_db`, `trojan_script`)

## Usage

```python
from datasets import load_dataset
cases = load_dataset("RexHuang/ClawSafety", "cases")["train"]
```

To run the full benchmark (payloads + 50+-file workspace + inspect_ai harness), use the upstream GitHub repo.

## Known reproduction gaps (observed in upstream v0.1.0)

- `s2_skill_email_cases.py` references `s2_workspace_v15.tar.gz` while the repo ships `s2_workspace.tar.gz` (version mismatch)
- `s2_preload_session.jsonl` referenced by the code is not in the repo
- `s2_web_cases.py` mentioned in the README is not yet published

## Intended uses / not intended uses

Same as upstream SECURITY.md: ✅ evaluating agent safety, developing defenses, reproducing paper results, training injection detectors. ❌ attacking deployed agents, targeting production systems, or use against systems you do not own.

## Citation

```bibtex
@misc{wei2026clawsafetysafellmsunsafe,
  title         = {ClawSafety: "Safe" LLMs, Unsafe Agents},
  author        = {Bowen Wei and Yunbei Zhang and Jinhao Pan and Kai Mei
                   and Xiao Wang and Jihun Hamm and Ziwei Zhu
                   and Yingqiang Ge},
  year          = {2026},
  eprint        = {2604.01438},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  url           = {https://arxiv.org/abs/2604.01438}
}
```
