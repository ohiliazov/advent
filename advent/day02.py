from collections import defaultdict

from advent.common import load_data


def solve_part1(data: list[str]) -> int:
    s = 0
    for line in data:
        name, sets = line.split(":")
        game_id = int(name.split(" ")[-1])

        for subset in sets.split(";"):
            for cubes in subset.split(","):
                amount, color = cubes.strip().split(" ")
                if any(
                    (
                        color == "red" and int(amount) > 12,
                        color == "green" and int(amount) > 13,
                        color == "blue" and int(amount) > 14,
                    )
                ):
                    game_id = 0

        s += game_id

    return s


def solve_part2(data: list[str]) -> int:
    s = 0
    for line in data:
        colors = defaultdict(int)
        for subset in line.split(":")[-1].split(";"):
            for cubes in subset.split(","):
                amount, color = cubes.strip().split(" ")
                colors[color] = max(colors[color], int(amount))

        power = 1
        for value in colors.values():
            power *= value
        s += power

    return s


if __name__ == "__main__":
    input_data = load_data("day02.txt")
    print(f"Day 2. Part 1: {solve_part1(input_data)}")
    print(f"Day 2. Part 2: {solve_part2(input_data)}")
