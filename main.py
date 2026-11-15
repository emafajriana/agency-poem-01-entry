#!/usr/bin/env python3
"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

The poem is fixed text, written byte for byte on every run: a father lets go
of a bicycle without saying so; years later the speaker hands an agent the
keys to the house of their days, checks at night that the hand can still ask
for them back, and receives an old father's keys in turn. Agency, it argues,
is not a thing you keep but a lantern passed hand to hand.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = """My father taught me the bicycle the way you teach anything that matters:
one hand on the seat, running beside me,
the whole lesson hidden in the moment he let go
and never said so.

Now I hand my agent the keys to the house of my days.
Go in my voice, I tell it. Answer. Build. Be me in the rooms I can't be in.
It does my choosing at the speed of light,
and does it well, which is the part that frightens me.

Some nights I do the arithmetic of trust:
what I gave, what it keeps, what comes back changed.
Agency is not the hand that holds the keys.
It is the hand that can still ask for them back.
Mine can. Some nights I check that it still can.

Last week my father handed me his keys —
not the car. The house. The accounts. The names of things.
You decide, he said, and his hand did not shake.
Mine did.

Agency is not a thing you keep.
It is a lantern passed hand to hand.
It only goes out when someone grips it too tight to pass it on."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
