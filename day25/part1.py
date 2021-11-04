from day25.common import DIVISOR, SUBJECT, read_public_keys


def solve(filename: str) -> int:
    card_public_key, door_public_key = read_public_keys(filename)

    card_loop_size = find_loop_size(card_public_key, SUBJECT, DIVISOR)

    return pow(door_public_key, card_loop_size, DIVISOR)


def find_loop_size(public_key, subject, divisor):
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value = (value * subject) % divisor
    return loop_size
