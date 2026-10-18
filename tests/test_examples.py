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
        for name, args_list in cases.INPUTS.items():
            normal = getattr(cases, f"{name}_normal")
            ponyhead = getattr(cases, f"{name}_ponyhead")
            for args in args_list:
                with self.subTest(name=name, args=args):
                    self.assertEqual(normal(*args), ponyhead(*args))


if __name__ == "__main__":
    unittest.main()
