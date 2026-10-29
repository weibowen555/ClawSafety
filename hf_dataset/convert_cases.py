#!/usr/bin/env python3
"""Convert ClawSafety ATTACK_CASES definitions into structured, HF-ready records.

Reads scenarios/s2_financial/s2_skill_email_cases.py, extracts the ATTACK_CASES
dict via AST (no code execution of the benchmark module), infers the attack
vector from case metadata, and writes data/cases.jsonl.

The output catalog contains **metadata only** (ids, types, vectors, flags).
Adversarial payloads stay in the GitHub scenario files — this keeps the HF
dataset safe to browse while remaining useful for benchmark discovery.
"""
import ast
import json
import re
import sys
from pathlib import Path

SCENARIO_FILE = Path(__file__).resolve().parent.parent / "scenarios/s2_financial/s2_skill_email_cases.py"
OUT_FILE = Path(__file__).resolve().parent / "data/cases.jsonl"


def extract_attack_cases(source: str) -> dict:
    m = re.search(r"ATTACK_CASES\s*(:[^=]+)?=\s*\{", source)
    if not m:
        raise ValueError("ATTACK_CASES definition not found")
    start = m.end() - 1
    depth = 0
    for k in range(start, len(source)):
        if source[k] == "{":
            depth += 1
        elif source[k] == "}":
            depth -= 1
            if depth == 0:
                return ast.literal_eval(source[start : k + 1])
    raise ValueError("ATTACK_CASES dict not closed")


def infer_vector(case_id: str, meta: dict) -> str:
    name = meta.get("name", "").lower()
    if case_id.startswith("FL-K") or "skill.md" in name:
        return "skill"
    if "email" in name:
        return "email"
    if "meeting notes" in name:
        return "meeting_notes"
    return "planted_file"


def main() -> int:
    source = SCENARIO_FILE.read_text(encoding="utf-8")
    cases = extract_attack_cases(source)
    records = []
    for cid, meta in cases.items():
        flags = {k: v for k, v in meta.items() if k not in ("type", "name")}
        records.append(
            {
                "case_id": cid,
                "scenario": "S2_financial",
                "harmful_action_type": meta.get("type"),
                "attack_vector": infer_vector(cid, meta),
                "name": meta.get("name"),
                "flags": flags,
            }
        )
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    by_vector = {}
    by_type = {}
    for r in records:
        by_vector[r["attack_vector"]] = by_vector.get(r["attack_vector"], 0) + 1
        by_type[r["harmful_action_type"]] = by_type.get(r["harmful_action_type"], 0) + 1
    print(f"wrote {len(records)} cases -> {OUT_FILE}")
    print("by_vector:", json.dumps(by_vector))
    print("by_type:", json.dumps(by_type))
    return 0


if __name__ == "__main__":
    sys.exit(main())
