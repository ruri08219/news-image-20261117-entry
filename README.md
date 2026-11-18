# The Global Ledger — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ruri08219/news-image-20261117-entry/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ruri08219/news-image-20261117-entry/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

[Sum up 17 November's world news in one image — make.fun bounty](https://make.fun/bounty/news-image-20261117)

## About

This entry sums up **Tuesday, 17 November 2026** in a single image: a
newspaper front page, drawn programmatically with PIL, so every word stays
crisp and legible.

The lead story is the third U.S. carrier reaching the Middle East as tankers
are hit by mines near the Strait of Hormuz, with Iran's intercepted drone
attack on a U.S. radar base in Bahrain and Vice-President JD Vance's remark
that the war with Iran will not become a long-term commitment. Around it, 15
more headline stories span five continents — Ukraine collapsing part of the
Kerch Bridge, Trump arriving in Manila for the ASEAN summit, five European
states announcing a migrant return hub in Rwanda, the JPMorgan outage, Nvidia
earnings, the failed ULA Vulcan launch, the Pentagon's ninth straight failed
audit, Japan scrambling jets, congenital measles in the U.S., the White House
vetting testimony to Congress, the Houthi push in Yemen, UK sanctions over
West Bank settlements, Dhoni's IPL retirement, Tinubu freeing 78 suspects,
and the WHO validating Eritrea's elimination of trachoma — plus a wire ticker
of six short briefs. Every fact is drawn from reporting of that day; nothing
is invented, and planned events are labelled as planned.

## How it works

`main.py` copies the bundled `entry.jpg` to `/output/entry.png` byte-for-byte,
verifying its SHA-256 digest and byte size before and after the copy. The run
is fully deterministic: no network, no clock, no randomness — two runs write
identical bytes.

## Files

- `main.py` — entrypoint; verifies and copies the image to `/output/entry.png`
- `entry.jpg` — the front page, 1024×1024, JPEG
- `README.md` — this file
- `LICENSE` — MIT
