from typing import List, Tuple


def read_instructions(filename: str) -> List[Tuple[str, int]]:
    with open(filename, "r") as file:
        return [(line[0], int(line[1:])) for line in file.readlines()]
