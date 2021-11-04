from typing import List

TREE = '#'


def read_map(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return [line.rstrip() for line in file]
