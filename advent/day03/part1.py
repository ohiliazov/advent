from pathlib import Path


INPUT_PATH = Path(__file__).parent / "input.txt"


def solve(data: list[str]) -> int:
    res = 0
    current_number = ""

    for row_idx, row in enumerate(data):
        for col_idx in range(len(row) + 1):
            if col_idx < len(row) and row[col_idx].isdigit():
                current_number += row[col_idx]
            elif current_number:
                lc = max(col_idx - len(current_number) - 1, 0)
                rc = min(col_idx + 1, len(row))
                lr = max(row_idx - 1, 0)
                rr = min(row_idx + 2, len(data))

                if any(
                    data[r][c] not in "0123456789."
                    for r in range(lr, rr)
                    for c in range(lc, rc)
                ):
                    res += int(current_number)

                current_number = ""

    return res


if __name__ == "__main__":
    s = 0
    with INPUT_PATH.open() as f:
        data = [line.strip() for line in f.readlines()]

    print(solve(data))
