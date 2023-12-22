from functools import partial

from advent.common import load_data


def process_pattern(pattern: list[str], smudge_fixed: bool) -> int:
    if res := find_mirror(pattern, smudge_fixed):
        return res * 100

    rotated = []
    for r in range(len(pattern[0])):
        row = ""
        for c in range(len(pattern)):
            row += pattern[c][r]
        rotated.append(row)

    return find_mirror(rotated, smudge_fixed)


def find_mirror(pattern: list[str], smudge_fixed: bool) -> int:
    for idx in range(1, len(pattern)):
        if is_mirror(pattern, idx, smudge_fixed):
            return idx
    return 0


def is_mirror(pattern: list[str], idx: int, smudge_fixed: bool) -> bool:
    for left, right in zip(pattern[idx - 1 :: -1], pattern[idx:]):
        if left != right:
            if smudge_fixed:
                return False

            for left_cell, right_cell in zip(left, right):
                if left_cell != right_cell:
                    if smudge_fixed:
                        return False

                    smudge_fixed = True

    return smudge_fixed


class Solution:
    def __init__(self, data: list[str]):
        self.patters = self.process_data(data)

    def process_data(self, data) -> list[list[str]]:
        patterns = []
        current_pattern = []
        for line in data:
            if line:
                current_pattern.append(line)
            else:
                patterns.append(current_pattern)
                current_pattern = []
        if current_pattern:
            patterns.append(current_pattern)
        return patterns

    def solve_part1(self):
        return sum(
            map(partial(process_pattern, smudge_fixed=True), self.patters)
        )

    def solve_part2(self):
        return sum(
            map(partial(process_pattern, smudge_fixed=False), self.patters)
        )


if __name__ == "__main__":
    input_data = load_data("day13.txt")
    board = Solution(input_data)
    print(f"Day 13. Part 1: {board.solve_part1()}")
    print(f"Day 13. Part 2: {board.solve_part2()}")
