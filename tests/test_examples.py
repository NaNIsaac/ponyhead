"""A tiny real equivalence check for README's *fixed example*."""
import runpy
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def capture(path: Path) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        runpy.run_path(str(path), run_name="__main__")
    return buffer.getvalue()


class ExampleTest(unittest.TestCase):
    def test_fixed_example(self):
        self.assertEqual(capture(EXAMPLES / "normal.py"), capture(EXAMPLES / "ponyhead.py"))
        self.assertEqual(capture(EXAMPLES / "ponyhead.py"), "1\n2\n3\n4\n5\n")


if __name__ == "__main__":
    unittest.main()
