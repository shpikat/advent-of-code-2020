import bisect
from collections import deque
from typing import List


def read_numbers() -> List[int]:
    with open("input", "r") as file:
        return [int(line.rstrip()) for line in file.readlines()]


def get_invalid_number(numbers: List[int]) -> int:
    preamble_size = 25
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
