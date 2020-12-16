from day15.common import read_starting_numbers, get_nth_number


def main():
    starting_numbers = read_starting_numbers()
    print(get_nth_number(starting_numbers, 2020))


if __name__ == "__main__":
    main()
