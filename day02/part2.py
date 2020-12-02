from day02.common import read_passwords


def main():
    passwords = read_passwords()

    valid_count = 0
    for (position1, position2, letter, password) in passwords:
        if (password[position1 - 1] == letter) != (password[position2 - 1] == letter):
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()
