from typing import List

FLOOR = '.'
SEAT = 'L'
OCCUPIED = '#'


def read_seats_layout(filename: str) -> List[List[str]]:
    with open(filename, "r") as file:
        return [list(line.rstrip()) for line in file.readlines()]
