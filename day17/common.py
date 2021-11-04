from typing import List

INACTIVE = '.'
ACTIVE = '#'


def read_initial_state(filename: str) -> List[List[str]]:
    with open(filename, "r") as file:
        return [list(line) for line in file.read().split('\n') if line]
