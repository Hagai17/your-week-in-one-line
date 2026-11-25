"""Your Week in One Line — entry for u-boge-your-week-in-one-line-d1c14ced.

Writes the single winning line (99 characters, inside the 100-character gate)
to /output/entry.txt and prints it. The line was picked by duelling twelve
drafts pairwise in both orders under the competition's published judge brief,
then duelling the champion against a sample of live field entries; the full
record is in candidates.md.
"""

import os

# The week, summed up: a new skill taught, a habit formed, and one emoji
# deployed with absolutely no sense of occasion.
LINE = (
    "I taught my dad emojis this week; he now ends every text "
    "with the dynamite one, even about grandma."
)


def main():
    text = LINE
    assert 1 <= len(text) <= 100, "entry must fit the 100-character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
