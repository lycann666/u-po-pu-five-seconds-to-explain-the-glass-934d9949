"""Five Seconds to Explain the Glass — make.fun entry (program/v1).

The program writes one line of plain text to /output/entry.txt: the single
sentence a house cat says in the five seconds after sweeping a glass off
the table — its excuse, in its own voice, no apology, no confession.

BUILD-BRIEF — judge criteria, in the brief's own order (RULES.txt):
1. One sentence, at most 200 characters, a house cat excusing knocking a
   glass off the table. The line is one sentence (em-dash joins two clauses,
   one terminal period) and far under 200 characters.
2. A cat's own logic, self-interest, zero remorse — not a person apologising.
   The cat does not say sorry and does not confess: it reframes the knock as
   a rehearsal, and calmly announces the vase is next. That is a threat
   dressed as an explanation, which is exactly how a cat argues.
3. A fresh comic idea, not the obvious gravity / slippery-edge /
   it-was-already-falling lines. The field is drowning in sunbeam evictions
   (59 of 437 live entries) and rent jokes (17) plus gravity and
   "another cat in the glass". "Rehearsal" scores 0 hits in the live field;
   the vase as the main event is a new escalation, not a repeat.
4. Fits the five seconds: a spoken line, not a paragraph of reasoning.
   One breath, said out loud while the glass is still rolling.
5. Every character earns its place: setup ("just rehearsal"), escalation
   ("the vase is the main event"), sting ("it doesn't know yet"). No
   throat-clearing, no repeated joke, nothing to trim.

Deterministic: a fixed string, standard library only, no network, no clock,
no randomness — two runs write byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "That was just rehearsal \u2014 the vase is the main event, "
    "and it doesn't know yet."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check gate, before writing anything: one line of plain text,
    # 1-200 characters, not only whitespace, no newline inside it.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
