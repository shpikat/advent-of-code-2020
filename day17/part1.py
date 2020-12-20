import itertools
from dataclasses import dataclass
from typing import Set

from day17.common import read_initial_state, INACTIVE, ACTIVE


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    z: int


def main():
    initial_state = read_initial_state()

    grid = {Coordinate(x, y, 0)
            for y, line in enumerate(initial_state)
            for x, value in enumerate(line)
            if value == '#'}

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
                    current = ACTIVE if Coordinate(x, y, z) in grid else INACTIVE
                    count = count_neighbourhood(grid, x, y, z)
                    if current == ACTIVE and (count != 2 + 1) and (count != 3 + 1):
                        elements_to_remove.append(Coordinate(x, y, z))
                    elif current == INACTIVE and count == 3:
                        elements_to_add.append(Coordinate(x, y, z))
                        next_min_x, next_max_x = min(next_min_x, x), max(next_max_x, x)
                        next_min_y, next_max_y = min(next_min_y, y), max(next_max_y, y)
                        next_min_z, next_max_z = min(next_min_z, z), max(next_max_z, z)
        grid.update(elements_to_add)
        grid.difference_update(elements_to_remove)

    print(len(grid))


def count_neighbourhood(grid: Set[Coordinate], x: int, y: int, z: int) -> int:
    """ Count all active cubes in the neighbourhood, including the center. """
    return sum(1 for dx, dy, dz in (itertools.product((-1, 0, 1), repeat=3))
               if Coordinate(x + dx, y + dy, z + dz) in grid)


if __name__ == "__main__":
    main()
