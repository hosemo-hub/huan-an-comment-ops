#!/usr/bin/env python3
"""Calculate auditable comment-thread metrics from a normalized JSON batch."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

CONSTRUCTIVE = {"story", "question", "correction", "insight", "dissent"}
SOCIAL = {"affiliation", "play"}


def ratio(numerator: int, denominator: int):
    return None if denominator == 0 else round(numerator / denominator, 4)


def calculate(payload: dict) -> dict:
    comments = payload.get("comments", [])
    types = Counter(c.get("contribution_type", "unclassified") for c in comments)
    audience = [c for c in comments if c.get("author_role") != "creator"]
    creator = [c for c in comments if c.get("author_role") == "creator"]
    roots = [c for c in audience if not c.get("parent_id")]
    replied_root_ids = {c.get("parent_id") for c in comments if c.get("parent_id")}
    return {
        "counts": {
            "all_comments": len(comments),
            "audience_comments": len(audience),
            "creator_comments": len(creator),
            "audience_roots": len(roots),
            "contribution_types": dict(types),
        },
        "rates": {
            "constructive_ratio": ratio(sum(types[t] for t in CONSTRUCTIVE), len(audience)),
            "social_ratio": ratio(sum(types[t] for t in SOCIAL), len(audience)),
            "noise_ratio": ratio(types["spam"], len(audience)),
            "harm_ratio": ratio(types["harm"], len(audience)),
            "threaded_ratio": ratio(sum(c.get("id") in replied_root_ids for c in roots), len(roots)),
            "author_reply_rate": ratio(len(creator), len(roots)),
            "substantive_author_reply_rate": ratio(sum(bool(c.get("substantive")) for c in creator), len(creator)),
            "new_information_rate": ratio(sum(bool(c.get("thread_has_new_information")) for c in roots), len(roots)),
        },
        "quality_flags": {
            "unclassified_comments": types["unclassified"],
            "stop_breach_count": sum(bool(c.get("stop_breach")) for c in comments),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = calculate(json.loads(args.input.read_text(encoding="utf-8")))
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
