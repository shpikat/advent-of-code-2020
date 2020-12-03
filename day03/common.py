from typing import List

TREE = '#'


def read_map() -> List[str]:
    with open("input", "r") as file:
        return [line.rstrip() for line in file]
