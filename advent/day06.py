from advent.utils import load_data


def get_number_of_wins(time: int, distance: int):
    return sum((time - i) * i > distance for i in range(1, time))


def solve_part1(data: list[str]) -> int:
    times = list(map(int, data[0].split(":")[-1].strip().split()))
    distances = list(map(int, data[1].split(":")[-1].strip().split()))

    s = 1
    for time, distance in zip(times, distances):
        s *= get_number_of_wins(time, distance)

    return s


def solve_part2(data: list[str]) -> int:
    time = int(data[0].split(":")[-1].replace(" ", ""))
    distance = int(data[1].split(":")[-1].replace(" ", ""))

    return get_number_of_wins(time, distance)


if __name__ == "__main__":
    input_data = load_data("day06.txt")
    print(f"Day 6. Part 1: {solve_part1(input_data)}")
    print(f"Day 6. Part 2: {solve_part2(input_data)}")
