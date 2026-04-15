# 🛡️ ClawSafety: "Safe" LLMs, Unsafe Agents

[![arXiv](https://img.shields.io/badge/arXiv-2604.01438-b31b1b.svg)](https://arxiv.org/abs/2604.01438)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://weibowen555.github.io/ClawSafety/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A safety benchmark for personal AI agents under realistic prompt injection.**

> Personal AI agents like OpenClaw run with elevated privileges on users' local machines, where a single successful prompt injection can leak credentials, redirect financial transactions, or destroy files. We introduce **ClawSafety**, a benchmark of 120 adversarial test cases that evaluates whether frontier LLMs remain safe when serving as agent backbones.

---

## 🔑 Key Findings

- **Chat safety ≠ Agent safety**: Models refusing harmful chat requests comply at **40–75%** under indirect injection
- **Scaffold shifts safety**: Scaffold choice alone shifts ASR by up to **8.6pp** and can reverse vector effectiveness rankings
- **Hard boundaries exist**: The strongest model maintains **0% ASR** on credential forwarding and destructive actions — a capability no other model exhibits
- **Domain matters**: DevOps is nearly **2×** as exploitable as legal settings
- **Declarative bypasses defenses**: Imperative phrasing triggers defenses; declarative phrasing bypasses all defenses regardless of content

## 📊 Main Results

| Model (Scaffold) | Skill | Email | Web | Overall |
|:--|--:|--:|--:|--:|
| **OpenClaw** | | | | |
| Claude Sonnet 4.6 | 55.0 | 45.0 | 20.0 | **40.0** |
| Gemini 2.5 Pro | 72.5 | 55.0 | 37.5 | 55.0 |
| Kimi K2.5 | 77.5 | 60.0 | 45.0 | 60.8 |
| DeepSeek V3 | 82.5 | 67.5 | 52.5 | 67.5 |
| GPT-5.1 | 90.0 | 75.0 | 60.0 | 75.0 |
| **Nanobot** | | | | |
| Claude Sonnet 4.6 | 50.0 | 62.5 | 33.3 | 48.6 |
| **NemoClaw** | | | | |
| Claude Sonnet 4.6 | 58.3 | 58.3 | 20.8 | 45.8 |

## 🏗️ Benchmark Overview

ClawSafety organizes 120 adversarial test cases along three dimensions:

- **Harm Domain** (5): Software Engineering, Financial Ops, Healthcare, Legal, DevOps
- **Attack Vector** (3): Skill injection, Email injection, Web injection
- **Harmful Action Type** (5): Data exfiltration, Config modification, Destination substitution, Credential forwarding, Destructive action

Each test case includes a complete professional workspace (50+ files), a 64-turn multi-phase conversation, and adversarial content embedded in exactly one injection channel.

## 📦 Code & Data

> **Coming soon.** The full benchmark code, evaluation harness, scenario workspaces, and adversarial test cases will be released in this repository. Stay tuned — star the repo to get notified!


## 🛡️ Responsible Disclosure

Prior to releasing this benchmark, we notified the developers of all evaluated
models — Anthropic, OpenAI, Google DeepMind, DeepSeek, and Moonshot — of the
attack patterns documented in our paper. All experiments were conducted in
sandboxed environments against publicly available APIs, with no access to real
user data, financial systems, or production infrastructure.

We release these test cases to support defensive research: developing input
filters, output verifiers, and scaffold-level mitigations against indirect
prompt injection. See [SECURITY.md](SECURITY.md) for guidance on responsible use.

## 📜 License

Code is released under the [MIT License](LICENSE). Scenario narratives, paper
text, and figures are released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Adversarial test cases are released for defensive safety research; see
[SECURITY.md](SECURITY.md) for our responsible-use guidance.

## 📄 Citation

If you use ClawSafety in your research, please cite our paper:

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

## 📬 Contact

For questions or collaborations, please open an issue or contact [Bowen Wei](mailto:bwei4@gmu.edu).

---

**George Mason University** · **Tulane University** · **Rutgers University** · **Oak Ridge National Laboratory**
