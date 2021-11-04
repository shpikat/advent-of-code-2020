from typing import List


def read_starting_numbers(filename: str) -> List[int]:
    with open(filename, "r") as file:
        return [int(number) for number in file.read().split(',')]


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
