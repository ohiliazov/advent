from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def find_number(s: str):
    i, j = 0, -1
    while not s[i].isdigit():
        i += 1
    while not s[j].isdigit():
        j -= 1
    return s[i] + s[j]


if __name__ == '__main__':
    with INPUT_PATH.open() as f:
        for line in f.readlines():
            print(find_number(line))
