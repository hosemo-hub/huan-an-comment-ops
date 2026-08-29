#!/usr/bin/env python3
"""Report robust within-account breakout statistics without cross-platform scoring."""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path


def quartiles(values: list[float]) -> tuple[float, float]:
    if len(values) < 2:
        return values[0], values[0]
    q = statistics.quantiles(values, n=4, method="inclusive")
    return q[0], q[2]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON with target and baseline numeric values")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    target = float(data["target"])
    baseline = [float(v) for v in data["baseline"]]
    if not baseline:
        raise SystemExit("baseline must contain at least one value")
    median = statistics.median(baseline)
    q1, q3 = quartiles(baseline)
    result = {
        "metric": data.get("metric", "unknown"),
        "target": target,
        "baseline_n": len(baseline),
        "baseline_min": min(baseline),
        "baseline_median": median,
        "baseline_max": max(baseline),
        "baseline_q1": q1,
        "baseline_q3": q3,
        "breakout_multiple": None if median == 0 else round(target / median, 4),
        "warning": "Descriptive within-account evidence, not causal proof.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
