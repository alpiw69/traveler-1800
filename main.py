"""make.fun bounty: One Sentence for a Traveler from 1800.

Deterministic, no-network program. Writes one sentence of at most
200 characters to /output/entry.txt, explaining the modern internet
to someone who just stepped out of the year 1800.

Every word in it is one a person from 1800 could know: letters,
voices, pictures, thin wires, horses, the sea. No internet, no
computer, no phone, no screen. The picture is a post office that
runs faster than any horse: anything can reach anyone, at once.
Running twice writes identical bytes.
"""
from pathlib import Path

SENTENCE = "Imagine every letter, voice and picture in the world racing along thin wires faster than any horse, so you can speak to a stranger across the sea as if he stood right beside you."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(SENTENCE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(SENTENCE)} chars)")


if __name__ == "__main__":
    main()
