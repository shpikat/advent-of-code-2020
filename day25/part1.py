from day25.common import read_public_keys, DIVISOR, SUBJECT


def main():
    card_public_key, door_public_key = read_public_keys()

    card_loop_size = find_loop_size(card_public_key, SUBJECT, DIVISOR)

    print(pow(door_public_key, card_loop_size, DIVISOR))


def find_loop_size(public_key, subject, divisor):
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value = (value * subject) % divisor
    return loop_size


if __name__ == "__main__":
    main()
