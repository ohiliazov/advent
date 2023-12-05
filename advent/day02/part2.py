from pathlib import Path
from collections import defaultdict

INPUT_PATH = Path(__file__).parent / "input.txt"


def solve(line: str) -> int:
    colors = defaultdict(int)
    for subset in line.split(":")[-1].split(";"):
        for cubes in subset.split(","):
            amount, color = cubes.strip().split(" ")
            colors[color] = max(colors[color], int(amount))

    power = 1
    for value in colors.values():
        power *= value
    return power


if __name__ == '__main__':
    s = 0
    with INPUT_PATH.open() as f:
        for line in f.readlines():
            s += solve(line)

    print(s)
