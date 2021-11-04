from day01.common import read_expenses


def solve(filename: str) -> int:
    expenses = read_expenses(filename)

    expenses.sort()
    for index_third, third in enumerate(expenses):
        target = 2020 - third
        little = 0
        big = len(expenses) - 1
        if little == index_third:
            little += 1
        if big == index_third:
            big -= 1
        while little < big:
            current = expenses[little] + expenses[big]
            if current < target:
                little += 1
                if little == index_third:
                    little += 1
            elif current > target:
                big -= 1
                if big == index_third:
                    big -= 1
            else:
                return expenses[little] * expenses[big] * third
    else:
        print("No three items summing 2020 are detected")
