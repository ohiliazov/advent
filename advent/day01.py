import re

from advent.common import load_data

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solve_part1(data: list[str]):
    regex = re.compile(r"\d")

    s = 0
    for line in data:
        matches = regex.findall(line)
        s += int(matches[0] + matches[-1])

    return s


def solve_part2(data: list[str]):
    regex = re.compile(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    )

    s = 0
    for line in data:
        matches = regex.findall(line)
        p1, p2 = matches[0], matches[-1]
        s += int(digits.get(p1, p1) + digits.get(p2, p2))

    return s


if __name__ == "__main__":
    input_data = load_data("day01.txt")
    print(f"Day 1. Part 1: {solve_part1(input_data)}")
    print(f"Day 1. Part 2: {solve_part2(input_data)}")
