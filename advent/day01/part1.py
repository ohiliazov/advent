import re
from pathlib import Path
from typing import Iterator

INPUT_PATH = Path(__file__).parent / "input.txt"


def load_lines() -> Iterator[str]:
    with INPUT_PATH.open() as f:
        return (line.strip() for line in f.readlines())


def solve():
    s = 0
    for line in load_lines():
        matches = re.findall(r"\d", line)
        s += int(matches[0] + matches[-1])

    return s


if __name__ == "__main__":
    print(solve())
