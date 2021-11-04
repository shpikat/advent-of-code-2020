from day09.common import get_invalid_number, read_numbers


def solve(filename: str) -> int:
    preamble_size = 5 if filename.endswith("sample.txt") else 25
    numbers = read_numbers(filename)
    return get_invalid_number(numbers, preamble_size)
