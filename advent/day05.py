from pathlib import Path

from advent.utils import load_data

INPUT_PATH = Path(__file__).parent / "input.txt"


def get_seeds(line: str) -> set[int]:
    _, line = line.split(":")
    return set(map(int, line.strip().split(" ")))


def collect_ranges(data: list[str]):
    all_lines = []

    lines = []
    for idx, line in enumerate(data[1:]):
        if line and line[0].isdigit():
            lines.append(line)
        elif lines:
            all_lines.append(lines)
            lines = []

    all_lines.append(lines)

    return all_lines


def parse_range_line(line: str) -> tuple[int, ...]:
    return tuple(map(int, line.strip().split(" ")))


def process_part1(lines: list[str], seeds: set[int]) -> set:
    new_seeds = set()

    for line in lines:
        dest_start, source_start, range_length = parse_range_line(line)
        source_end = source_start + range_length

        for seed in seeds.copy():
            if seed in range(source_start, source_end):
                new_seeds.add(seed - source_start + dest_start)
                seeds.remove(seed)

    return new_seeds | seeds


def solve_part1(data: list[str]) -> int:
    seeds = get_seeds(data[0])

    for lines in collect_ranges(data[1:]):
        seeds = process_part1(lines, seeds)

    return min(seeds)


def get_seed_ranges(line: str) -> set[tuple[int, int]]:
    _, line = line.split(":")
    data = list(map(int, line.strip().split(" ")))

    seeds = set()
    for idx in range(0, len(data), 2):
        seeds.add((data[idx], data[idx + 1]))

    return seeds


def process_part2(
    lines: list[str], seed_ranges: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    new_seed_ranges = set()

    for line in lines:
        dest_start, source_start, range_length = parse_range_line(line)
        source_end = source_start + range_length

        for seed_start, seed_length in seed_ranges.copy():
            seed_end = seed_start + seed_length

            if seed_start > source_end or seed_end < source_start:
                continue

            seed_ranges.remove((seed_start, seed_length))

            if seed_start < source_start:
                seed_ranges.add((seed_start, source_start - seed_start))
                seed_start = source_start

            if seed_end > source_end:
                seed_ranges.add((source_end, seed_end - source_end))
                seed_end = source_end

            new_seed_ranges.add(
                (
                    seed_start + dest_start - source_start,
                    seed_end - seed_start,
                )
            )

    return new_seed_ranges | seed_ranges


def solve_part2(data: list[str]) -> int:
    seed_ranges = get_seed_ranges(data[0])

    for lines in collect_ranges(data[1:]):
        seed_ranges = process_part2(lines, seed_ranges)

    return min([seed[0] for seed in seed_ranges])


if __name__ == "__main__":
    input_data = load_data("day05.txt")
    print(f"Day 5. Part 1: {solve_part1(input_data)}")
    print(f"Day 5. Part 2: {solve_part2(input_data)}")
