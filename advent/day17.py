from advent.utils import load_data
from enum import Enum
from queue import PriorityQueue

Coord = tuple[int, int]


class Direction(Enum):
    horizontal = (0, 1)
    vertical = (1, 0)

    @property
    def next_direction(self) -> "Direction":
        return self.vertical if self is self.horizontal else self.horizontal

    def __repr__(self):
        return self.name

    def __lt__(self, other: "Direction") -> bool:
        return True


class Solution:
    def __init__(self, data: list[str]):
        self.grid = data
        self.size = len(self.grid)

    def get_heat_loss(self, coord: Coord) -> int:
        row, column = coord
        return -int(self.grid[row][column])

    def is_valid_coord(self, coord: Coord) -> bool:
        row, column = coord
        return -1 < row < self.size and -1 < column < self.size

    def _get_neighbours(
        self,
        source: tuple[int, int, Direction],
        multiply: int,
        min_step: int,
        max_step: int,
    ):
        row, column, direction = source
        vertical, horizontal = direction.value
        heat_loss = 0
        graph_part = {}

        for step in range(1, max_step):
            next_row = row + vertical * step * multiply
            next_column = column + horizontal * step * multiply
            target = (next_row, next_column, direction.next_direction)

            if 0 <= next_row < self.size and 0 <= next_column < self.size:
                heat_loss += int(self.grid[next_row][next_column])
                if step >= min_step:
                    graph_part[target] = heat_loss
            else:
                break

        return graph_part

    def neighbours(
        self, source: tuple[int, int, Direction], min_step: int, max_step: int
    ):
        return {
            **self._get_neighbours(source, -1, min_step, max_step),
            **self._get_neighbours(source, 1, min_step, max_step),
        }

    def solve(self, min_step: int, max_step: int):
        pq = PriorityQueue()
        pq.put_nowait((0, (0, 0, Direction.horizontal)))
        pq.put_nowait((0, (0, 0, Direction.vertical)))

        visited = set()

        while True:
            acc_heat_loss, u = pq.get_nowait()
            if u[0] == self.size - 1 and u[1] == self.size - 1:
                return acc_heat_loss

            if u not in visited:
                visited.add(u)
                for v, heat_loss in self.neighbours(
                    u, min_step, max_step
                ).items():
                    if v not in visited:
                        pq.put_nowait((acc_heat_loss + heat_loss, v))

    def solve_part1(self):
        return self.solve(1, 4)

    def solve_part2(self):
        return self.solve(4, 11)


if __name__ == "__main__":
    input_data = load_data("day17.txt")
    board = Solution(input_data)
    print(f"Day 17. Part 1: {board.solve_part1()}")
    print(f"Day 17. Part 2: {board.solve_part2()}")
