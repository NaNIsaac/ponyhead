"""Measure every normal/Ponyhead pair in examples/cases.py: lines of code and time per call.

python scripts/bench.py

Prints a Markdown table for the README. Times are the best of 7 runs over each pair's
test inputs, so they depend on the machine and Python version printed above the table.
"""

import inspect
import platform
import sys
import timeit
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))

import cases


def body_lines(fn) -> int:
    lines = inspect.getsource(fn).splitlines()[1:]  # skip the def line
    return sum(1 for line in lines if line.strip() and not line.strip().startswith("#"))


def per_call_ns(fn, args_list) -> float:
    def run():
        for args in args_list:
            fn(*args)

    number = max(1, 20_000 // len(args_list))
    best = min(timeit.repeat(run, number=number, repeat=7))
    return best / (number * len(args_list)) * 1e9


def main() -> None:
    print(f"Python {platform.python_version()} on {platform.system()} {platform.machine()}\n")
    print("| Case | Lines | Time per call | Ponyhead ÷ normal |")
    print("| --- | --- | --- | --- |")
    total_n = total_p = 0
    for name, args_list in cases.INPUTS.items():
        normal, ponyhead = getattr(cases, f"{name}_normal"), getattr(cases, f"{name}_ponyhead")
        ln, lp = body_lines(normal), body_lines(ponyhead)
        tn, tp = per_call_ns(normal, args_list), per_call_ns(ponyhead, args_list)
        total_n, total_p = total_n + ln, total_p + lp
        print(f"| `{name}` | {ln} → {lp} | {tn:.0f} → {tp:.0f} ns | {tp / tn:.1f}× |")
    print(f"| **all** | **{total_n} → {total_p}** | | |")


if __name__ == "__main__":
    main()
