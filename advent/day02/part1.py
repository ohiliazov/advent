from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def solve(line: str) -> int:
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


if __name__ == "__main__":
    s = 0
    with INPUT_PATH.open() as f:
        for line in f.readlines():
            s += solve(line)

    print(s)
