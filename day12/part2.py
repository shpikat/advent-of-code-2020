from math import cos, radians, sin
from typing import Tuple

from day12.common import read_instructions

actions = {
    'N': lambda ship, waypoint, value: (ship, (waypoint[0], waypoint[1] - value)),
    'S': lambda ship, waypoint, value: (ship, (waypoint[0], waypoint[1] + value)),
    'E': lambda ship, waypoint, value: (ship, (waypoint[0] + value, waypoint[1])),
    'W': lambda ship, waypoint, value: (ship, (waypoint[0] - value, waypoint[1])),
    'L': lambda ship, waypoint, value: (ship, rotate(waypoint, -value)),
    'R': lambda ship, waypoint, value: (ship, rotate(waypoint, value)),
    'F': lambda ship, waypoint, value: ((ship[0] + waypoint[0] * value, ship[1] + waypoint[1] * value), waypoint),
}


def rotate(point: Tuple[int, int], angle_degrees: int) -> Tuple[int, int]:
    x, y = point
    angle_radians = radians(angle_degrees)
    angle_sine = sin(angle_radians)
    angle_cosine = cos(angle_radians)
    return round(x * angle_cosine - y * angle_sine), round(y * angle_cosine + x * angle_sine)


def solve(filename: str) -> int:
    instructions = read_instructions(filename)

    ship = (0, 0)
    waypoint = (10, -1)

    for action, value in instructions:
        ship, waypoint = actions[action](ship, waypoint, value)

    return abs(ship[0]) + abs(ship[1])
