from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def solve(line: str):
    i, j = 0, -1
    while not line[i].isdigit():
        i += 1
    while not line[j].isdigit():
        j -= 1
    return int(line[i] + line[j])


if __name__ == "__main__":
    s = 0
    with INPUT_PATH.open() as f:
        for line in f.readlines():
            s += solve(line)

    print(s)
