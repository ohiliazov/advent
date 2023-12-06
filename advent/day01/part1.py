import re

from advent.utils import load_data


def solve(data: list[str]):
    s = 0
    for line in data:
        matches = re.findall(r"\d", line)
        s += int(matches[0] + matches[-1])

    return s


if __name__ == "__main__":
    input_data = load_data("day01.txt")
    print(solve(input_data))
