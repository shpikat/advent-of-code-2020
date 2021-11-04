from collections import deque

from day09.common import get_invalid_number, read_numbers


def solve(filename: str) -> int:
    preamble_size = 5 if filename.endswith("sample.txt") else 25
    numbers = read_numbers(filename)

    target_sum = get_invalid_number(numbers, preamble_size)

    window = deque()
    window_sum = 0
    it = iter(numbers)
    while window_sum != target_sum:
        if window_sum > target_sum:
            window_sum -= window.popleft()
        elif window_sum < target_sum:
            number = next(it)
            window.append(number)
            window_sum += number
    return min(window) + max(window)
