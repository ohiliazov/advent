from collections import defaultdict

from advent.utils import load_data


def solve_line(line: str) -> int:
    colors = defaultdict(int)
    for subset in line.split(":")[-1].split(";"):
        for cubes in subset.split(","):
            amount, color = cubes.strip().split(" ")
            colors[color] = max(colors[color], int(amount))

    power = 1
    for value in colors.values():
        power *= value
    return power


def solve(data: list[str]) -> int:
    return sum(solve_line(line) for line in data)


if __name__ == "__main__":
    input_data = load_data("day02.txt")
    print(solve(input_data))
