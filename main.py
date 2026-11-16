#!/usr/bin/env python3
"""Create reproducible train, validation, and test CSV splits."""
from __future__ import annotations
import argparse, csv, math, random, sys
from collections import defaultdict
from pathlib import Path

def allocate(count: int, ratios: tuple[float, float, float]):
    raw = [count * ratio for ratio in ratios]
    sizes = [math.floor(value) for value in raw]
    remainder = count - sum(sizes)
    order = sorted(range(3), key=lambda i: raw[i] - sizes[i], reverse=True)
    for index in order[:remainder]: sizes[index] += 1
    return sizes[0], sizes[1], sizes[2]

def split_rows(rows, ratios, seed, label_column):
    rng = random.Random(seed); groups = defaultdict(list)
    if label_column:
        for row in rows: groups[row[label_column]].append(row)
    else: groups["__all__"] = list(rows)
    outputs = ([], [], [])
    for group in groups.values():
        rng.shuffle(group); a, b, c = allocate(len(group), ratios)
        outputs[0].extend(group[:a]); outputs[1].extend(group[a:a+b]); outputs[2].extend(group[a+b:a+b+c])
    for output in outputs: rng.shuffle(output)
    return outputs

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path); parser.add_argument("--output-dir", type=Path, default=Path("split-data"))
    parser.add_argument("--label-column"); parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--train", type=float, default=0.8); parser.add_argument("--validation", type=float, default=0.1)
    parser.add_argument("--test", type=float, default=0.1); args = parser.parse_args()
    ratios = (args.train, args.validation, args.test)
    if any(value < 0 for value in ratios) or not math.isclose(sum(ratios), 1.0, abs_tol=1e-8):
        parser.error("train, validation, and test ratios must be non-negative and sum to 1")
    if not args.input.is_file(): parser.error(f"input file does not exist: {args.input}")
    try:
        with args.input.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames: raise ValueError("CSV must include a header row")
            if args.label_column and args.label_column not in reader.fieldnames: raise ValueError(f"label column not found: {args.label_column}")
            rows = list(reader); headers = reader.fieldnames
        outputs = split_rows(rows, ratios, args.seed, args.label_column)
        args.output_dir.mkdir(parents=True, exist_ok=True)
        names = ("train.csv", "validation.csv", "test.csv")
        for name, subset in zip(names, outputs):
            with (args.output_dir / name).open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=headers); writer.writeheader(); writer.writerows(subset)
    except (OSError, csv.Error, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr); return 2
    print(f"Seed: {args.seed}")
    for name, subset in zip(names, outputs): print(f"{name:14} {len(subset):>6} rows")
    print(f"Total rows: {len(rows)}"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
