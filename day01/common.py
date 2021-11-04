from typing import List


def read_expenses(filename: str) -> List[int]:
    with open(filename, "r") as file:
        return [int(line) for line in file]
