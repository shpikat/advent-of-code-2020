from day09.common import read_numbers, get_invalid_number


def main():
    numbers = read_numbers()

    print(get_invalid_number(numbers))


if __name__ == "__main__":
    main()
