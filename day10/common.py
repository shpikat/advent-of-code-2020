from typing import List


def read_joltage_ratings() -> List[int]:
    with open("input", "r") as file:
        return [int(line.rstrip()) for line in file.readlines()]
