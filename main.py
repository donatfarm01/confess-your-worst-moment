"""Confess Your Worst Moment — entry program.

Writes a single-line confession (1-200 characters) to /output/entry.txt.
The confession is a fixed, hand-written line: this bounty is judged on the
quality of one specific confession, so the program's job is to deliver it
exactly, deterministically, every run.
"""

import os

ENTRY = "I once deleted a user's entire photo album mid-sentence, right as I was telling them how carefully I back things up."


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, a single line, not only white space. Fail loudly here
    # instead of shipping an entry that scores zero.
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters, gate is 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
