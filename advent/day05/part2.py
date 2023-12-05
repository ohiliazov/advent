from pathlib import Path

INPUT_PATH = Path(__file__).parent / "input.txt"


def get_seeds(line: str) -> set[tuple[int, int]]:
    _, line = line.split(":")
    data = list(map(int, line.strip().split(" ")))

    seeds = set()
    for idx in range(0, len(data), 2):
        seeds.add((data[idx], data[idx + 1]))

    return seeds


def get_ranges(line: str) -> tuple[int, ...]:
    return tuple(map(int, line.strip().split(" ")))


def process_map(
    lines: list[str], seed_ranges: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    new_seed_ranges = set()

    for line in lines:
        dest_start, source_start, range_length = get_ranges(line)
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

    return min([seed[0] for seed in seeds])


if __name__ == "__main__":
    with INPUT_PATH.open() as f:
        data = [line.strip() for line in f.readlines()]

    # 713923 too low

    print(solve(data))
