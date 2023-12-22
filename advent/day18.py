from advent.common import load_data
from common import Coord, Direction

DIRECTIONS = {
    "U": Direction.UP,
    "3": Direction.UP,
    "L": Direction.LEFT,
    "2": Direction.LEFT,
    "R": Direction.RIGHT,
    "0": Direction.RIGHT,
    "D": Direction.DOWN,
    "1": Direction.DOWN,
}


class Solution:
    def __init__(self, data: list[str]):
        self.lines = data

    def process_part1(self, line: str) -> tuple[Coord, int]:
        direction, depth, _ = line.split()
        return DIRECTIONS[direction].value, int(depth)

    def process_part2(self, line: str) -> tuple[Coord, int]:
        hex_code = line.split()[-1][2:-1]
        depth, direction = int(hex_code[:-1], base=16), hex_code[-1]
        return DIRECTIONS[direction].value, int(depth)

    def solve(self, process_func: callable):
        boundary = 0
        coord = Coord(x=0, y=0)
        corners = []
        for line in self.lines:
            direction, depth = process_func(line)
            boundary += depth
            coord = coord + direction * depth
            corners.append(coord)

        n = len(corners)
        area = 0
        for i in range(n):
            c1 = corners[i]
            c2 = corners[i - 1]
            area += int(c1.x * c2.y) - int(c2.x * c1.y)

        return (abs(area) + boundary) // 2 + 1

    def solve_part1(self):
        return self.solve(self.process_part1)

    def solve_part2(self):
        return self.solve(self.process_part2)


if __name__ == "__main__":
    input_data = load_data("day18.txt")
    board = Solution(input_data)
    print(f"Day 18. Part 1: {board.solve_part1()}")
    print(f"Day 18. Part 2: {board.solve_part2()}")
