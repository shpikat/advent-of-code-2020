from day01.common import read_expenses


def main():
    expenses = read_expenses()

    expenses.sort()
    for index_third, third in enumerate(expenses):
        target = 2020 - third
        little = 0
        big = len(expenses) - 1
        while little < big:
            current = expenses[little] + expenses[big]
            if current < target:
                little += 1
            elif current > target:
                big -= 1
            else:
                print(expenses[little] * expenses[big] * third)
                return
    else:
        print("No three items summing 2020 are detected")


if __name__ == "__main__":
    main()
