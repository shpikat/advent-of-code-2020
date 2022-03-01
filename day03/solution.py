from typing import Iterable, List

TREE = "#"


def part1(input_data: str) -> int:
    map_input = read_map(input_data)
    x = 0
    wrap_at = len(map_input[0])
    count = 0

    for line in with_first_element_skipped(map_input):
        x = (x + 3) % wrap_at
        if line[x] == TREE:
            count += 1
    return count


def part2(input_data: str) -> int:
    map_input = read_map(input_data)
    wrap_at = len(map_input[0])

    slopes = [
        (lambda y: True, lambda x: (x + 1) % wrap_at),
        (lambda y: True, lambda x: (x + 3) % wrap_at),
        (lambda y: True, lambda x: (x + 5) % wrap_at),
        (lambda y: True, lambda x: (x + 7) % wrap_at),
        (lambda y: y % 2 == 0, lambda x: (x + 1) % wrap_at),
    ]
    current_x = [0] * len(slopes)
    counts = [0] * len(slopes)

    for current_y, line in enumerate(map_input):
        if current_y == 0:
            continue
        for i, slope in enumerate(slopes):
            is_applicable, get_next_x = slope
            if is_applicable(current_y):
                current_x[i] = get_next_x(current_x[i])
                if line[current_x[i]] == TREE:
                    counts[i] += 1

    result = 1
    for count in counts:
        result *= count
    return result


def with_first_element_skipped(a_list: List[str]) -> Iterable[str]:
    an_iterator = iter(a_list)
    next(an_iterator)
    return an_iterator


def read_map(input_data: str) -> List[str]:
    return [line.rstrip() for line in input_data.splitlines()]
