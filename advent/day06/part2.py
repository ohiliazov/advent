from pathlib import Path

INPUT_PATH = Path(__file__).parent / "input.txt"


def get_number(line: str) -> int:
    line = line.split(":")[-1]
    return int(line.replace(" ", ""))


def get_number_of_wins(time: int, distance: int):
    return sum((time - i) * i > distance for i in range(time + 1))


def solve(data: list[str]) -> int:
    time = get_number(data[0])
    distance = get_number(data[1])

    return get_number_of_wins(time, distance)


if __name__ == "__main__":
    with INPUT_PATH.open() as f:
        data = [line.strip() for line in f.readlines()]

    print(solve(data))
