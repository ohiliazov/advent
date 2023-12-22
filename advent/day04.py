from collections import defaultdict

from advent.common import load_data


def get_common_numbers(line: str) -> set[int]:
    _, line = line.split(":")
    part1, part2 = line.split("|")
    set1 = set([int(item.strip()) for item in part1.strip().split()])
    set2 = set([int(item.strip()) for item in part2.strip().split()])
    return set1 & set2


def solve_part1(data: list[str]) -> int:
    res = 0

    for line in data:
        match = get_common_numbers(line)

        if match:
            res += 2 ** (len(match) - 1)

    return res


def solve_part2(data: list[str]) -> int:
    cards = defaultdict(lambda: 1)

    for idx, line in enumerate(data):
        match = get_common_numbers(line)

        current_number = cards[idx]
        for i in range(idx + 1, min(idx + 1 + len(match), len(data))):
            cards[i] += current_number

    return sum(cards.values())


if __name__ == "__main__":
    input_data = load_data("day04.txt")
    print(f"Day 4. Part 1: {solve_part1(input_data)}")
    print(f"Day 4. Part 2: {solve_part2(input_data)}")
