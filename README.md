# Off-Key Angels

[![make.fun](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/Akhmad045/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/Akhmad045/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

An entry for the [make.fun bounty "Famous Last Words: The Funniest Epitaph"](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406) — the funniest possible famous last words, carved as one tombstone epitaph of at most 150 characters.

## The epitaph

> I can hear the angels singing. They're off-key.

47 characters and 47 bytes. The output file holds exactly that line, with no trailing newline.

## How it was picked

Twelve candidate last words were drafted and compared pairwise against the judge's brief. The winner is a dying man reporting what he hears on the other side: the heavenly choir, the soundtrack of every deathbed scene, turns out to be badly sung. It is one line of dying speech, the laugh lands on a single read from a genuine incongruity rather than a pun or a sad sentiment, the second sentence undercuts the first, it reads exactly like something carved on a stone, and it is short enough to repeat to a friend. It steers clear of the genre's recycled lines — no "I told you I was sick", no wifi or password joke, no "finally some peace and quiet" — and at 47 bytes it also wins any exact tie on size.

## Running it

```sh
python3 main.py --self-test  # check the gate, then write the file
python3 main.py               # just write /output/entry.txt
```

`main.py` checks the line against the gate (1–150 characters, one line, no control or invisible characters), writes it to `/output/entry.txt` in UTF-8, and reads the file back to prove the bytes match. `--self-test` runs the gate over fifteen known good and bad inputs first.

Built with referral code `4g7knchf`.

## License

MIT. The full text is in [LICENSE](LICENSE).
