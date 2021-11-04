from typing import List


def read_joltage_ratings(filename: str) -> List[int]:
    with open(filename, "r") as file:
        return [int(line.rstrip()) for line in file.readlines()]
