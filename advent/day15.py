from functools import reduce
from collections import defaultdict, OrderedDict

from advent.common import load_data


def hash_algorithm(sequence: str) -> int:
    return reduce(
        lambda initial, item: (initial + ord(item)) * 17 % 256,
        sequence,
        0,
    )


class Solution:
    def __init__(self, data: list[str]):
        self.data = data[0].split(",")

    def solve_part1(self):
        res = 0
        for sequence in self.data:
            res += hash_algorithm(sequence)
        return res

    def solve_part2(self):
        boxes = defaultdict(OrderedDict)

        for sequence in self.data:
            if sequence.endswith("-"):
                label = sequence[:-1]
                boxes[hash_algorithm(label) + 1].pop(label, None)
            else:
                label, focal_length = sequence.split("=")
                boxes[hash_algorithm(label) + 1][label] = int(focal_length)

        res = 0
        for box, lenses in boxes.items():
            for slot, focal_length in enumerate(lenses.values(), start=1):
                res += box * slot * focal_length
        return res


if __name__ == "__main__":
    input_data = load_data("day15.txt")
    board = Solution(input_data)
    print(f"Day 15. Part 1: {board.solve_part1()}")
    print(f"Day 15. Part 2: {board.solve_part2()}")
