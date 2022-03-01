import bisect
from collections import deque
from typing import List


def part1(input_data: str, preamble_size: int) -> int:
    numbers = read_numbers(input_data)
    return get_invalid_number(numbers, preamble_size)


def part2(input_data: str, preamble_size: int) -> int:
    numbers = read_numbers(input_data)

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


def read_numbers(input_data: str) -> List[int]:
    return [int(line.rstrip()) for line in input_data.splitlines()]


def get_invalid_number(numbers: List[int], preamble_size: int) -> int:
    preamble = numbers[:preamble_size]
    window = deque(preamble)
    preamble.sort()
    for number in numbers[preamble_size:]:
        if has_sum_of_two(preamble, number):
            to_remove = window.popleft()
            del preamble[bisect.bisect_left(preamble, to_remove)]
            window.append(number)
            bisect.insort(preamble, number)
        else:
            return number


def has_sum_of_two(lst: List[int], target: int) -> bool:
    little = 0
    big = len(lst) - 1
    while little < big:
        current = lst[little] + lst[big]
        if current < target:
            little += 1
        elif current > target:
            big -= 1
        else:
            return True
    else:
        return False
