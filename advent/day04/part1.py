from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def solve(data: list[str]) -> int:
    res = 0

    for line in data:
        _, line = line.split(":")
        winning, have = line.split("|")
        winning_set = set([int(item.strip()) for item in winning.strip().split()])
        have_set = set([int(item.strip()) for item in have.strip().split()])

        match = winning_set & have_set
        if match:
            res += 2 ** (len(match) - 1)

    return res


if __name__ == "__main__":
    with INPUT_PATH.open() as f:
        data = [line.strip() for line in f.readlines()]

    print(solve(data))
