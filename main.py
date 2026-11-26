"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the fridge to /output/entry.txt.
The line is one sentence of 115 characters, inside the 1-200 gate.
"""
import os

LINE = "My fridge has one job — keep things cold — yet the ice cream melts, the lettuce freezes, and the butter has filed for divorce twice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
