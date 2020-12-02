from day02.common import read_passwords


def main():
    passwords = read_passwords()

    valid_count = 0
    for (min_count, max_count, letter, password) in passwords:
        password_count = password.count(letter)
        if min_count <= password_count <= max_count:
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()
