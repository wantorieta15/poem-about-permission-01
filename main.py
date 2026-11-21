"""Write the poem about permission to /output/entry.txt.

The poem is about agency: the power to ask and to be given. A speaker
places a sparrow in someone's open hands and asks them not to close them;
the gift turns out to be not the bird, but the right to open them.
"""

import os

POEM = """Permission

You asked to hold a sparrow.
I placed it in your hands
and said, Don't close them.

Its heart beat
against your lifeline.
You held the ache
of not keeping it.

Then it rose.
You stood, hands
still open. The gift
was never the bird —
the right to open them."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
