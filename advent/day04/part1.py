from advent.utils import load_data


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
    input_data = load_data("day04.txt")
    print(solve(input_data))
