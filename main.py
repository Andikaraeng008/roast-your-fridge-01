"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the fridge to /output/entry.txt.
The line is one sentence of 115 characters, inside the 1-200 gate.
"""
import os

LINE = "My fridge hums all night like it is warming up for a choir, then bills me for the concert on the electricity meter."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
