from math import cos, radians, sin

from day12.common import read_instructions

actions = {
    'N': lambda angle, x, y, value: (angle, x, y - value),
    'S': lambda angle, x, y, value: (angle, x, y + value),
    'E': lambda angle, x, y, value: (angle, x + value, y),
    'W': lambda angle, x, y, value: (angle, x - value, y),
    'L': lambda angle, x, y, value: (angle - value, x, y),
    'R': lambda angle, x, y, value: (angle + value, x, y),
    'F': lambda angle, x, y, value: (angle,
                                     x + round(sin(radians(angle))) * value,
                                     y + round(cos(radians(angle))) * value),
}


def solve(filename: str) -> int:
    instructions = read_instructions(filename)

    angle = 0
    x = 0
    y = 0
    for action, value in instructions:
        angle, x, y = actions[action](angle, x, y, value)

    return abs(x) + abs(y)
