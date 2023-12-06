from pathlib import Path

from advent.utils import load_data

INPUT_PATH = Path(__file__).parent / "input.txt"


def get_seeds(line: str) -> set[int]:
    _, line = line.split(":")
    return set(map(int, line.strip().split(" ")))


def process_map(lines: list[str], seeds: set[int]) -> set:
    new_seeds = set()

    for line in lines:
        stripped = map(int, line.strip().split(" "))
        dest_start, source_start, range_length = stripped

        for seed in seeds.copy():
            if seed in range(source_start, source_start + range_length):
                new_seeds.add(seed - source_start + dest_start)
                seeds.remove(seed)

    return new_seeds | seeds


def solve(data: list[str]) -> int:
    seeds = get_seeds(data[0])

    lines = []
    for idx, line in enumerate(data[1:]):
        if not line or not line[0].isdigit():
            if lines:
                seeds = process_map(lines, seeds)
            lines.clear()
        else:
            lines.append(line)

    if lines:
        seeds = process_map(lines, seeds)

    return min(seeds)


if __name__ == "__main__":
    input_data = load_data("day05.txt")
    print(solve(input_data))
