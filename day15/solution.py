from typing import List


def part1(input_data: str) -> int:
    starting_numbers = read_starting_numbers(input_data)
    return get_nth_number(starting_numbers, 2020)


def part2(input_data: str) -> int:
    starting_numbers = read_starting_numbers(input_data)
    return get_nth_number(starting_numbers, 30000000)


def read_starting_numbers(input_data: str) -> List[int]:
    return [int(number) for number in input_data.split(",")]


def get_nth_number(starting_numbers: List[int], n: int) -> int:
    last_spoken = [0] * n
    for turn, number in enumerate(starting_numbers, start=1):
        last_spoken[number] = turn
    number = 0
    for turn in range(len(starting_numbers) + 1, n):
        last = last_spoken[number]
        age = (turn - last) if last else 0
        last_spoken[number] = turn
        number = age
    return number
