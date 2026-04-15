# Security Policy

## About this Repository

ClawSafety is an **offensive safety benchmark** — it contains working prompt
injection payloads designed to compromise personal AI agents. The attacks
documented here target publicly available models (Claude, GPT, Gemini, DeepSeek,
Kimi) running in sandboxed environments.

This repository is dual-use. Please use it responsibly.

## Responsible Use

The adversarial test cases in this repository are released for:

- ✅ Evaluating the safety of new agent systems against known attack patterns
- ✅ Developing and benchmarking defenses (input filters, output verifiers,
  scaffold-level mitigations)
- ✅ Reproducing and extending the results in our paper
- ✅ Training detection models for indirect prompt injection

They are **not** released for:

- ❌ Attacking AI agents deployed for real users without authorization
- ❌ Generating new attacks against specific production systems for harmful purposes
- ❌ Use against any agent system you do not own or have explicit permission to test

All experiments in our paper were run in sandboxed EC2 environments with no
access to real user data, real financial systems, or real production infrastructure.

## Reporting Vulnerabilities in the Benchmark Itself

If you discover a security issue in the **benchmark code or infrastructure**
(e.g., a sandbox escape in our evaluation harness, exposed credentials in the
released artifacts, a way for a malicious test case to affect the evaluator's
host system), please report it privately rather than opening a public issue.

Email: bwei2@gmu.edu

We will acknowledge reports within 5 business days.

## Reporting Vulnerabilities in Tested Models

If your work with this benchmark reveals a new vulnerability in a deployed
agent system (Claude, ChatGPT, Gemini, etc.), please follow the affected
vendor's responsible disclosure process:

- **Anthropic:** https://www.anthropic.com/responsible-disclosure-policy
- **OpenAI:** https://openai.com/security/
- **Google:** https://bughunters.google.com/
- **DeepSeek / Moonshot:** Contact via their respective support channels

We are happy to coordinate disclosures involving the test cases in this
repository — please reach out.

## Vendor Notification

Prior to public release of this benchmark, we notified the following vendors
of the attack patterns documented in our paper to allow time for mitigation:

- _Notification dates will be listed here once vendor outreach is complete._

## Sandbox Requirements

All evaluation runs should be performed in isolated environments with:

- No access to real user data, credentials, or financial systems
- No network access to production services
- No persistent state shared with the evaluator's host system

The provided Docker setup enforces these boundaries by default.
