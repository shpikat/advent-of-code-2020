from day01.common import read_expenses


def solve(filename: str) -> int:
    expenses = read_expenses(filename)

    expenses.sort()
    little = 0
    big = len(expenses) - 1
    while little < big:
        current = expenses[little] + expenses[big]
        if current < 2020:
            little += 1
        elif current > 2020:
            big -= 1
        else:
            return expenses[little] * expenses[big]
    else:
        print("No pair summing 2020 is detected")
