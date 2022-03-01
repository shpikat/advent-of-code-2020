from math import cos, radians, sin
from typing import List, Tuple


def part1(input_data: str) -> int:
    instructions = read_instructions(input_data)

    actions = {
        "N": lambda _angle, _x, _y, _value: (_angle, _x, _y - _value),
        "S": lambda _angle, _x, _y, _value: (_angle, _x, _y + _value),
        "E": lambda _angle, _x, _y, _value: (_angle, _x + _value, _y),
        "W": lambda _angle, _x, _y, _value: (_angle, _x - _value, _y),
        "L": lambda _angle, _x, _y, _value: (_angle - _value, _x, _y),
        "R": lambda _angle, _x, _y, _value: (_angle + _value, _x, _y),
        "F": lambda _angle, _x, _y, _value: (
            _angle,
            _x + round(sin(radians(_angle))) * _value,
            _y + round(cos(radians(_angle))) * _value,
        ),
    }

    angle = 0
    x = 0
    y = 0
    for action, value in instructions:
        angle, x, y = actions[action](angle, x, y, value)

    return abs(x) + abs(y)


def rotate(point: Tuple[int, int], angle_degrees: int) -> Tuple[int, int]:
    x, y = point
    angle_radians = radians(angle_degrees)
    angle_sine = sin(angle_radians)
    angle_cosine = cos(angle_radians)
    return round(x * angle_cosine - y * angle_sine), round(y * angle_cosine + x * angle_sine)


def part2(input_data: str) -> int:
    instructions = read_instructions(input_data)

    actions = {
        "N": lambda _ship, _waypoint, _value: (_ship, (_waypoint[0], _waypoint[1] - _value)),
        "S": lambda _ship, _waypoint, _value: (_ship, (_waypoint[0], _waypoint[1] + _value)),
        "E": lambda _ship, _waypoint, _value: (_ship, (_waypoint[0] + _value, _waypoint[1])),
        "W": lambda _ship, _waypoint, _value: (_ship, (_waypoint[0] - _value, _waypoint[1])),
        "L": lambda _ship, _waypoint, _value: (_ship, rotate(_waypoint, -_value)),
        "R": lambda _ship, _waypoint, _value: (_ship, rotate(_waypoint, _value)),
        "F": lambda _ship, _waypoint, _value: (
            (_ship[0] + _waypoint[0] * _value, _ship[1] + _waypoint[1] * _value),
            _waypoint,
        ),
    }

    ship = (0, 0)
    waypoint = (10, -1)

    for action, value in instructions:
        ship, waypoint = actions[action](ship, waypoint, value)

    return abs(ship[0]) + abs(ship[1])


def read_instructions(input_data: str) -> List[Tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in input_data.splitlines()]
