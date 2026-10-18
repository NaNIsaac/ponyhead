<h1 align="center">Ponyhead</h1>

<p align="center"><em>Sees nothing. Writes everything. It works (probably).</em></p>

<p align="center"><strong>The AI coding skill that puts the code back.</strong></p>

<p align="center">
  <img src="assets/ponyhead-avatar.png" alt="Ponyhead: an earnest coder with oval glasses, visible dark pupils, and a ponytail tied forward over the face" width="230" />
</p>

<p align="center"><sub>Why use a loop when you can copy and paste?</sub></p>

<p align="center">
  <img src="assets/ponyhead-demo.gif" alt="Animated terminal comparison: a loop becomes five print statements, an even check reads the last digit, a positive check runs twice, and 3 * 4 becomes 4 + 4 + 4" width="760" />
</p>

---

[Ponytail](https://github.com/DietrichGebert/ponytail) teaches coding agents to write less code. **Ponyhead puts the code back.**

Meet the developer who ties their ponytail *in front* of their face, hides behind slightly crooked glasses, and tackles every problem with the confidence of someone who has never heard of a helper function.

Ponyhead is an **opt-in parody Agent Skill** that encourages comically beginner-like code: repetitive, over-literal, and remarkably devoted to copy-paste. It doesn't run a model, phone home, or need an API key. It just asks your existing coding agent to take the scenic route.

## Before / after

**Normal agent:**

```python
for i in range(1, 6):
    print(i)
```

**Ponyhead:**

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Same output **for this fixed example**. More lines. More effort. Absolutely no shame.

### Not just loops

| Normal | Ponyhead |
| --- | --- |
| `n % 2 == 0` | `str(n)[-1] in "02468"` *(even numbers end in an even digit, obviously)* |
| `return x > 0` | `if x > 0:` / `if (x > 0) == True: return True` / `else: return False` *(checked twice)* |
| `3 * 4` | `4 + 4 + 4` |
| `["Mon", ..., "Sun"][i]` | `if i == 0: return "Mon"` / `elif i == 1: ...` ×7 |
| `a, b = b, a` | `temp = a` / `temp2 = b` / `a = temp2` / `b = temp` |
| `max(a, b)` | `if a > b` / `elif b > a` / `elif a == b` |
| `abs(x)` | `if x < 0: return x * -1`, with zero handled separately |
| `not items` | `if len(items) == 0: return True` / `if len(items) != 0: return False` |
| `s[::-1]` | prepend one character at a time |

Full code in [`examples/cases.py`](examples/cases.py); each pair is checked for equal results in [`tests/test_examples.py`](tests/test_examples.py).

## Carefully engineered inefficiency

| Feature | Philosophy |
| --- | --- |
| **Hand-unrolled loops** | If the loop runs five times, the code can appear five times. |
| **Artisanal duplication** | Why reuse a function when you can lovingly rewrite it? |
| **Literal conditionals** | A dictionary lookup sounds suspiciously efficient. |
| **Bonus variables** | `result_final_really_final_2` needs a home. |
| **Suspiciously functional** | The style is a joke; correctness is not. |

## Install

Ponyhead uses the [Agent Skills](https://agentskills.io/specification) `SKILL.md` format.

Install it with the Skills CLI:

```bash
npx skills add NaNIsaac/ponyhead --skill ponyhead
```

Or install specifically for Claude Code in your current project:

```bash
npx skills add NaNIsaac/ponyhead --skill ponyhead -a claude-code
```

**Manual install:** Copy [`skills/ponyhead/SKILL.md`](skills/ponyhead/SKILL.md) to `.claude/skills/ponyhead/SKILL.md` in your Claude Code project, or to the corresponding skills directory in another compatible agent.

## Try it

```text
/ponyhead Rewrite this fixed five-item example in Ponyhead style.

/ponyhead lite Make this snippet more beginner-like. Keep it short.

/ponyhead full Make this toy example gloriously repetitive. Up to 100 lines.
```

Ponyhead is **opt-in**. In Claude Code the skill never activates on its own; type `/ponyhead`. Other agents may accept a plain request such as **"Use Ponyhead for this example."**

| Mode | Behavior |
| --- | --- |
| `lite` (default) | One compact, intentionally clumsy example, typically 8–30 lines. |
| `full` | More enthusiastic repetition, capped at approximately 100 illustrative lines. |

## The Ponyhead rule

> **Be hilariously inexperienced, not irresponsibly incorrect.**

Keep the toy example's observable behavior intact; don't delete checks, weaken validation, invent guarantees, or introduce vulnerabilities. Prefer snippets and previews rather than editing important files. No destructive operations or production refactors without explicit authorization.

This is an affectionate joke about **overly verbose code**, not about any group of developers.

## Development

```bash
python -m unittest discover -s tests   # fixed-example equivalence check
python scripts/bench.py                # lines and time per call for every pair
uv run scripts/build_demo.py           # regenerate the demo GIF
```

## Benchmark results

We did eventually run it. Every pair in [`examples/cases.py`](examples/cases.py), timed on the same
inputs the tests check (Python 3.14.7 on Windows AMD64):

| Case | Lines | Time per call | Ponyhead ÷ normal |
| --- | --- | --- | --- |
| `is_even` | 1 → 1 | 96 → 186 ns | 1.9× |
| `is_positive` | 1 → 5 | 72 → 89 ns | 1.2× |
| `twelve` | 1 → 1 | 133 → 133 ns | 1.0× |
| `day_name` | 1 → 14 | 143 → 139 ns | 1.0× |
| `swap` | 2 → 5 | 83 → 98 ns | 1.2× |
| `bigger` | 1 → 6 | 101 → 82 ns | 0.8× |
| `absolute` | 1 → 5 | 81 → 91 ns | 1.1× |
| `is_empty` | 1 → 4 | 88 → 126 ns | 1.4× |
| `reverse` | 1 → 4 | 173 → 302 ns | 1.7× |
| **all** | **10 → 45** | | |

Ponyhead writes 4.5× the lines and is *not* reliably slower: `day_name` no longer builds a list on
every call and `bigger` skips a function call, so a few cases get faster. Reproduce with
`python scripts/bench.py`; numbers move a little between runs and machines.

### Benchmark results (marketing edition)

| Metric | Result |
| --- | --- |
| Lines of code | ↑↑↑ |
| Loop appreciation | ↓↓↓ |
| Copy-paste craftsmanship | Handcrafted |
| Confidence | Untested, yet immense |
| Controlled performance comparison | We copied the benchmark 47 times and forgot to run it. |

*All figures here are jokes, not empirical performance results.*

## Credits

An independent parody inspired by [Ponytail](https://github.com/DietrichGebert/ponytail) and its fewer-lines philosophy. **Not affiliated with, sponsored by, or endorsed by the Ponytail maintainers.** Ponyhead uses separately created mascot artwork.

## License

MIT — see [LICENSE](LICENSE).
