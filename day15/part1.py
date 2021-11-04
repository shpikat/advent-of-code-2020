from day15.common import get_nth_number, read_starting_numbers


def solve(filename: str) -> int:
    starting_numbers = read_starting_numbers(filename)
    return get_nth_number(starting_numbers, 2020)
