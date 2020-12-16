from typing import List


def read_starting_numbers() -> List[int]:
    with open("input", "r") as file:
        return [int(number) for number in file.read().split(',')]


def get_nth_number(starting_numbers: List[int], n: int) -> int:
    last_spoken = {number: turn for turn, number in enumerate(starting_numbers, start=1)}
    number = 0
    for turn in range(len(starting_numbers) + 1, n):
        age = turn - last_spoken.get(number, turn)
        last_spoken[number] = turn
        number = age
    return number
