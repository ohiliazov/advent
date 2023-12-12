import functools
import re

from advent.utils import load_data


@functools.cache
def process_record(record: str, groups: tuple[int]):
    if not groups:
        return int("#" not in record)

    size, *remaining = groups
    group_regex = re.compile(rf"[#?]{{{size}}}[.?]")

    to_idx = len(record) - sum(remaining) - len(remaining)
    if hash_idx := record.find("#") + 1:
        to_idx = min(hash_idx, to_idx)

    count = 0
    for idx in range(to_idx):
        if m := group_regex.match(record, pos=idx):
            end = m.end()
            count += process_record(record[end:], tuple(remaining))

    return count


class Solution:
    def __init__(self, data: list[str]):
        self.records = data

    def parse_line(self, line: str, multiply: int) -> tuple[str, list[int]]:
        record, groups = line.split()
        return "?".join(record for _ in range(multiply)) + ".", list(
            map(int, groups.split(","))
        ) * multiply

    def solve_line(self, line: str, multiply: int) -> int:
        record, target_groups = self.parse_line(line, multiply)
        return process_record(record, tuple(target_groups))

    def solve_part1(self):
        return sum(map(lambda line: self.solve_line(line, 1), self.records))

    def solve_part2(self):
        return sum(map(lambda line: self.solve_line(line, 5), self.records))


if __name__ == "__main__":
    input_data = load_data("day12.txt")
    board = Solution(input_data)
    print(f"Day 12. Part 1: {board.solve_part1()}")
    print(f"Day 12. Part 2: {board.solve_part2()}")
