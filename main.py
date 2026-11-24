"""The One-Line Cat Joke That Lands - make.fun entry.

Writes a single cat joke, one line, under 200 characters, to
/output/entry.txt. Pure stdlib, no network, fully deterministic.
"""

import os

JOKE = ("I told my cat he was adopted. He blinked once, then knocked "
        "my phone off the table \u2014 apparently the feeling was mutual.")

DST = "/output/entry.txt"


def main():
    if not (1 <= len(JOKE) <= 200):
        raise ValueError("joke must be 1-200 characters, got %d" % len(JOKE))
    if "\n" in JOKE.strip():
        raise ValueError("joke must be a single line")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print("wrote %s (%d chars)" % (DST, len(JOKE)))


if __name__ == "__main__":
    main()
