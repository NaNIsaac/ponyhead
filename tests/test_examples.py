"""Real equivalence checks for the README's fixed examples."""
import runpy
import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
sys.path.insert(0, str(EXAMPLES))

import cases

NUMBERS = range(-1000, 1001)
SMALL = range(-20, 21)


def capture(path: Path) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        runpy.run_path(str(path), run_name="__main__")
    return buffer.getvalue()


class ExampleTest(unittest.TestCase):
    def test_fixed_example(self):
        self.assertEqual(capture(EXAMPLES / "normal.py"), capture(EXAMPLES / "ponyhead.py"))
        self.assertEqual(capture(EXAMPLES / "ponyhead.py"), "1\n2\n3\n4\n5\n")

    def test_cases(self):
        inputs = {
            "is_even": [(n,) for n in NUMBERS],
            "is_positive": [(n,) for n in NUMBERS],
            "twelve": [()],
            "day_name": [(i,) for i in range(7)],
            "swap": [(a, b) for a in SMALL for b in SMALL],
            "bigger": [(a, b) for a in SMALL for b in SMALL],
            "absolute": [(n,) for n in NUMBERS],
            "is_empty": [([],), ([0],), ("",), ("x",), ((),)],
            "reverse": [("",), ("a",), ("hello",), ("가나다",)],
        }
        for name, args_list in inputs.items():
            normal = getattr(cases, f"{name}_normal")
            ponyhead = getattr(cases, f"{name}_ponyhead")
            for args in args_list:
                with self.subTest(name=name, args=args):
                    self.assertEqual(normal(*args), ponyhead(*args))


if __name__ == "__main__":
    unittest.main()
