import math
import sys

from advent.utils import load_data


def parse_line(line: str) -> tuple[str, dict[str, str]]:
    node, path = line.split(" = ")
    left, right = path.lstrip("(").rstrip(")").split(", ")

    return node, {"L": left, "R": right}


def solve(data: list[str], endswith: str) -> int:
    instructions = data[0]
    paths = dict(map(parse_line, data[2:]))
    nodes = {node for node in paths if node.endswith(endswith)}

    cycles = dict()
    for step in range(sys.maxsize):
        new_nodes = set()
        for node in nodes:
            node = paths[node][instructions[step % len(instructions)]]
            if node.endswith("Z"):
                cycles[node] = step + 1
                if len(cycles) == len(nodes):
                    return math.lcm(*cycles.values())
            new_nodes.add(node)
        nodes = new_nodes


def solve_part1(data: list[str]) -> int:
    return solve(data, "AAA")


def solve_part2(data: list[str]) -> int:
    return solve(data, "A")


if __name__ == "__main__":
    input_data = load_data("day08.txt")
    print(f"Day 8. Part 1: {solve_part1(input_data)}")
    print(f"Day 8. Part 2: {solve_part2(input_data)}")
