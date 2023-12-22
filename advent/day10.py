from advent.common import load_data

ANIMAL = "S"
NORTH = "S|LJ"
EAST = "S-LF"
WEST = "S-J7"
SOUTH = "S|7F"

Coord = tuple[int, int]


class Solution:
    def __init__(self, data: list[list[str] | str]):
        self.board = list(map(list, data))

    @property
    def height(self) -> int:
        return len(self.board)

    @property
    def width(self) -> int:
        return len(self.board[0])

    def get_adjacent(self, coord: Coord) -> list[Coord]:
        r, c = coord
        coords = []
        if r > 0:
            coords.append((r - 1, c))

        if c > 0:
            coords.append((r, c - 1))

        if r < self.height - 1:
            coords.append((r + 1, c))

        if c < self.width - 1:
            coords.append((r, c + 1))

        return coords

    def get_value(self, coord: Coord) -> str:
        r, c = coord
        return self.board[r][c]

    def set_value(self, coord: Coord, value: str):
        r, c = coord
        self.board[r][c] = value

    def is_connected(self, coord1: Coord, coord2: Coord) -> bool:
        r1, c1 = coord1
        r2, c2 = coord2
        v1 = self.get_value(coord1)
        v2 = self.get_value(coord2)

        if r1 == r2:
            if c2 - c1 == 1 and v1 in EAST and v2 in WEST:
                return True
            if c1 - c2 == 1 and v1 in WEST and v2 in EAST:
                return True
        if c1 == c2:
            if r2 - r1 == 1 and v1 in SOUTH and v2 in NORTH:
                return True
            if r1 - r2 == 1 and v1 in NORTH and v2 in SOUTH:
                return True
        return False

    def get_connected(self, coord1: Coord) -> list[Coord]:
        return list(
            filter(
                lambda coord2: self.is_connected(coord1, coord2),
                self.get_adjacent(coord1),
            )
        )

    def get_animal_coord(self) -> Coord:
        for r, row in enumerate(self.board):
            for c, value in enumerate(row):
                if value == ANIMAL:
                    return r, c

    def get_loop(self) -> set[Coord]:
        init_coord = self.get_animal_coord()

        loop = set()
        to_explore = {init_coord}

        while to_explore:
            coord = to_explore.pop()
            loop.add(coord)
            for connected in self.get_connected(coord):
                if connected not in loop:
                    to_explore.add(connected)

        return loop

    def solve_part1(self) -> int:
        loop = self.get_loop()
        return (len(loop) + 1) // 2

    def solve_part2(self):
        loop = self.get_loop()

        for r, row in enumerate(self.board):
            for c, value in enumerate(row):
                coord = r, c
                if coord not in loop:
                    self.set_value(coord, ".")

        new_board = []
        for r, row in enumerate(self.board):
            new_row = [".", row[0]]
            for c, value in enumerate(row[1:], start=1):
                coord = r, c
                prev_coord = r, c - 1
                if self.is_connected(coord, prev_coord):
                    new_row.append("-")
                else:
                    new_row.append(".")

                if coord in loop:
                    new_row.append(value)
                else:
                    new_row.append(".")

            new_row.append(".")
            new_board.append(new_row)

        new_board.insert(0, ["."] * (self.width * 2 + 1))

        for r in range(1, self.height):
            extra_row = ["."]
            for c in range(self.width):
                coord = r, c
                prev_coord = r - 1, c

                if self.is_connected(coord, prev_coord):
                    extra_row.append("|")
                else:
                    extra_row.append(".")
                extra_row.append(".")

            new_board.insert(r * 2, extra_row)

        self.board = new_board
        unfilled = {(0, 0)}

        while unfilled:
            coord = unfilled.pop()
            self.set_value(coord, " ")

            for connected in self.get_adjacent(coord):
                if self.get_value(connected) == ".":
                    unfilled.add(connected)

        inner_counter = 0
        for line in self.board[1::2]:
            for cell in line[1::2]:
                if cell == ".":
                    inner_counter += 1

        return inner_counter


if __name__ == "__main__":
    input_data = load_data("day10.txt")
    board = Solution(input_data)
    print(f"Day 10. Part 1: {board.solve_part1()}")
    print(f"Day 10. Part 2: {board.solve_part2()}")
