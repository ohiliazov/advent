from collections import defaultdict
from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def solve(data: list[str]) -> int:
    cards = defaultdict(lambda: 1)

    for idx, line in enumerate(data):
        _, line = line.split(":")
        winning, have = line.split("|")
        winning_set = set([int(item.strip()) for item in winning.strip().split()])
        have_set = set([int(item.strip()) for item in have.strip().split()])

        match = len(winning_set & have_set)

        current_number = cards[idx]
        for i in range(idx+1, min(idx+1+match, len(data))):
            cards[i] += current_number

    return sum(cards.values())


if __name__ == '__main__':
    with INPUT_PATH.open() as f:
        data = [line.strip() for line in f.readlines()]

    print(solve(data))
