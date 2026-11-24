"""Make the AI Judge Laugh: the Office Joke Open — make.fun entry.

Holds a single office joke, at most 200 characters. It is validated,
printed, and written to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os

JOKE = (
    "Our sprint retrospective ran three hours and produced one "
    "action item: schedule another retrospective."
)

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate accepts 1..200 characters of UTF-8 text.
MAX_CHARS = 200


def validate_joke(joke: str) -> str:
    """Validate the joke is 1..200 characters of non-blank text."""
    if not isinstance(joke, str):
        raise ValueError("joke must be a string")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not 1 <= len(joke) <= MAX_CHARS:
        raise ValueError(
            f"joke must be 1..{MAX_CHARS} characters, got {len(joke)}"
        )
    if not joke.strip():
        raise ValueError("joke must not be only white space")
    return joke


def main() -> None:
    joke = validate_joke(JOKE)
    print(joke)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
