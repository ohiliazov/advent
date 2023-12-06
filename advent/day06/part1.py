from pathlib import Path

INPUT_PATH = Path(__file__).parent / "input.txt"


def get_numbers(line: str) -> list[int]:
    line = line.split(":")[-1]
    return list(map(int, line.strip().split()))


def get_number_of_wins(time: int, distance: int):
    return sum((time - i) * i > distance for i in range(1, time))


def solve(data: list[str]) -> int:
    times = get_numbers(data[0])
    distances = get_numbers(data[1])

    s = 1
    for time, distance in zip(times, distances):
        s *= get_number_of_wins(time, distance)

    return s


if __name__ == "__main__":
    with INPUT_PATH.open() as f:
        data = [line.strip() for line in f.readlines()]

    print(solve(data))
