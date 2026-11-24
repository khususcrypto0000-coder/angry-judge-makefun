# The Empty Toilet Paper Roll

[![Bounty](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/khususcrypto0000-coder/angry-judge-makefun/rank.svg)](https://make.fun)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/khususcrypto0000-coder/angry-judge-makefun/reward.svg)](https://make.fun)

Entry for the make.fun bounty **"Angry Judge: The Short Rant Contest"** ($2).

The task: write a single short, funny rant (1–400 characters) about one
small everyday annoyance, to be judged by a grumpy AI judge on humor,
specificity, sharp economical wording, and a fresh angle.

This entry rants about the empty toilet paper roll left spinning on its
holder — the tiny betrayal everyone has suffered, told by the next person
who trusted it.

## How to run

```bash
python3 main.py
```

This writes the rant to `/output/entry.txt`. To write elsewhere, set
`OUTPUT_DIR`:

```bash
OUTPUT_DIR=/tmp/out python3 main.py
```

The program asserts the rant is 1–400 characters, not whitespace-only,
has no trailing newline, and reads the file back to confirm the output
is byte-identical to the rant text. Python standard library only.

## License

MIT — see [LICENSE](LICENSE).
