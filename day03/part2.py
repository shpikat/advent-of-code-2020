from day03.common import TREE, read_map


def solve(filename: str) -> int:
    map_input = read_map(filename)
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
