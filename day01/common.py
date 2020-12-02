from typing import List


def read_expenses() -> List[int]:
    with open("input", "r") as file:
        return [int(line) for line in file]
