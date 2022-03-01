from typing import Tuple

SUBJECT = 7
DIVISOR = 20201227


def part1(input_data: str) -> int:
    card_public_key, door_public_key = read_public_keys(input_data)

    card_loop_size = find_loop_size(card_public_key, SUBJECT, DIVISOR)

    return pow(door_public_key, card_loop_size, DIVISOR)


def find_loop_size(public_key, subject, divisor):
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value = (value * subject) % divisor
    return loop_size


def read_public_keys(input_data: str) -> Tuple[int, int]:
    lines = input_data.splitlines()
    return int(lines[0]), int(lines[1])
