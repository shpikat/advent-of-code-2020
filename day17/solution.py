import itertools
from dataclasses import dataclass
from typing import List, Set

INACTIVE = "."
ACTIVE = "#"


@dataclass(frozen=True)
class Coordinate3D:
    x: int
    y: int
    z: int


def part1(input_data: str) -> int:
    initial_state = read_initial_state(input_data)

    grid = {
        Coordinate3D(x, y, 0)
        for y, line in enumerate(initial_state)
        for x, value in enumerate(line)
        if value == "#"
    }

    next_min_x = next_min_y = next_min_z = 0
    next_max_x = len(initial_state[0])
    next_max_y = len(initial_state)
    next_max_z = 0

    for i in range(1, 6 + 1):
        elements_to_add = []
        elements_to_remove = []
        min_x, max_x = next_min_x, next_max_x
        min_y, max_y = next_min_y, next_max_y
        min_z, max_z = next_min_z, next_max_z

        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    current = ACTIVE if Coordinate3D(x, y, z) in grid else INACTIVE
                    count = count_neighbourhood_3d(grid, x, y, z)
                    if current == ACTIVE and (count != 2 + 1) and (count != 3 + 1):
                        elements_to_remove.append(Coordinate3D(x, y, z))
                    elif current == INACTIVE and count == 3:
                        elements_to_add.append(Coordinate3D(x, y, z))
                        next_min_x, next_max_x = min(next_min_x, x), max(next_max_x, x)
                        next_min_y, next_max_y = min(next_min_y, y), max(next_max_y, y)
                        next_min_z, next_max_z = min(next_min_z, z), max(next_max_z, z)
        grid.update(elements_to_add)
        grid.difference_update(elements_to_remove)

    return len(grid)


def count_neighbourhood_3d(grid: Set[Coordinate3D], x: int, y: int, z: int) -> int:
    """Count all active cubes in the neighbourhood, including the center."""
    return sum(
        1
        for dx, dy, dz in (itertools.product((-1, 0, 1), repeat=3))
        if Coordinate3D(x + dx, y + dy, z + dz) in grid
    )


@dataclass(frozen=True)
class Coordinate4D:
    x: int
    y: int
    z: int
    w: int


def part2(input_data: str) -> int:
    initial_state = read_initial_state(input_data)

    grid = {
        Coordinate4D(x, y, 0, 0)
        for y, line in enumerate(initial_state)
        for x, value in enumerate(line)
        if value == "#"
    }

    next_min_x = next_min_y = next_min_z = next_min_w = 0
    next_max_x = len(initial_state[0])
    next_max_y = len(initial_state)
    next_max_z = 0
    next_max_w = 0

    for i in range(1, 6 + 1):
        elements_to_add = []
        elements_to_remove = []
        min_x, max_x = next_min_x, next_max_x
        min_y, max_y = next_min_y, next_max_y
        min_z, max_z = next_min_z, next_max_z
        min_w, max_w = next_min_w, next_max_w

        for w in range(min_w - 1, max_w + 2):
            for z in range(min_z - 1, max_z + 2):
                for y in range(min_y - 1, max_y + 2):
                    for x in range(min_x - 1, max_x + 2):
                        current = ACTIVE if Coordinate4D(x, y, z, w) in grid else INACTIVE
                        count = count_neighbourhood_4d(grid, x, y, z, w)
                        if current == ACTIVE and (count != 2 + 1) and (count != 3 + 1):
                            elements_to_remove.append(Coordinate4D(x, y, z, w))
                        elif current == INACTIVE and count == 3:
                            elements_to_add.append(Coordinate4D(x, y, z, w))
                            next_min_x, next_max_x = min(next_min_x, x), max(next_max_x, x)
                            next_min_y, next_max_y = min(next_min_y, y), max(next_max_y, y)
                            next_min_z, next_max_z = min(next_min_z, z), max(next_max_z, z)
                            next_min_w, next_max_w = min(next_min_w, w), max(next_max_w, w)
        grid.update(elements_to_add)
        grid.difference_update(elements_to_remove)

    return len(grid)


def count_neighbourhood_4d(grid: Set[Coordinate4D], x: int, y: int, z: int, w: int) -> int:
    """Count all active cubes in the neighbourhood, including the center."""
    # For better performance the calculations can be short-circuited at the count specific for each case (4 or 5)
    return sum(
        1
        for dx, dy, dz, dw in (itertools.product((-1, 0, 1), repeat=4))
        if Coordinate4D(x + dx, y + dy, z + dz, w + dw) in grid
    )


def read_initial_state(input_data: str) -> List[List[str]]:
    return [list(line) for line in input_data.splitlines() if line]
