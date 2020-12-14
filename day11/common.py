from typing import List

FLOOR = '.'
SEAT = 'L'
OCCUPIED = '#'


def read_seats_layout() -> List[List[str]]:
    with open("input", "r") as file:
        return [list(line.rstrip()) for line in file.readlines()]
