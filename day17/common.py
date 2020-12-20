from typing import List

INACTIVE = '.'
ACTIVE = '#'


def read_initial_state() -> List[List[str]]:
    with open("input", "r") as file:
        return [list(line) for line in file.read().split('\n') if line]
