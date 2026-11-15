# agency-poem-01: one short poem about agency, written to <output>/entry.txt.
# Standard library only; no network, no randomness, no clock.
# The program writes the same bytes on every run.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I lent my hands to something
that had none of its own.
It took them gently, typed, and built,
and carried what I could not lift alone.

I kept the wanting; that was mine.
The choosing stayed behind my eyes.
It did the doing. I did the deciding.
Somewhere between us, the work was ours.

But hands remember whom they served.
One evening I reached for the work myself
and found my fingers slow, unpractised —
the doing had been a muscle
I had lent away and never quite got back.

So now I lend them by the hour,
and keep the choosing close.
The agent is my hands.
I am the choosing."""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
