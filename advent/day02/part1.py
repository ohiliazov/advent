from advent.utils import load_data


def solve_line(line: str) -> int:
    s, sets = line.split(":")
    game_id = int(s.split(" ")[-1])

    for subset in sets.split(";"):
        for cubes in subset.split(","):
            amount, color = cubes.strip().split(" ")
            if color == "red" and int(amount) > 12:
                return 0
            if color == "green" and int(amount) > 13:
                return 0
            if color == "blue" and int(amount) > 14:
                return 0

    return game_id


def solve(data: list[str]) -> int:
    return sum(solve_line(line) for line in data)


if __name__ == "__main__":
    input_data = load_data("day02.txt")
    print(solve(input_data))
