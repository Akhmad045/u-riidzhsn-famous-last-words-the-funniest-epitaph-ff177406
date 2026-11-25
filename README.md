# Off-Key Angels

[![make.fun](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/Akhmad045/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/Akhmad045/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

Entry for the [make.fun bounty "Famous Last Words: The Funniest Epitaph"](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406): the funniest possible famous last words as a single tombstone epitaph, at most 150 characters.

## The line

> I can hear the angels singing. They're off-key.

47 characters / 47 bytes — one short line, no trailing newline in the output file.

## Why it meets the brief

The dying man reports what he hears on the other side, and the heavenly choir — the soundtrack of every deathbed scene — turns out to be badly sung. It is a single line of dying speech carved in stone (criterion 1); the laugh lands on one read, from a genuine incongruity rather than a pun or a sad sentiment (criterion 2); the twist is the second sentence undercutting the first — angels, then off-key (criterion 3); it reads exactly like something carved on a stone, one short line with no stage directions and no explanation (criterion 4); and it is quotable enough to repeat to a friend (criterion 5). It avoids the genre's recycled lines — no "I told you I was sick", no wifi or password joke, no "finally some peace and quiet" — and at 47 bytes it also wins any exact tie on size.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # validates the gate and the written file
```

`main.py` writes exactly the line above to `/output/entry.txt` (UTF-8, no trailing newline) and read-checks the file it wrote. `--self-test` also checks the gate's rejection cases: empty, whitespace-only, over 150 characters, multi-line, carriage return, leading/trailing whitespace, control characters (including tab and DEL), and invisible format characters.

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
