from typing import List


def part1(input_data: str) -> int:
    expenses = read_expenses(input_data)

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


def part2(input_data: str) -> int:
    expenses = read_expenses(input_data)

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


def read_expenses(input_data: str) -> List[int]:
    return [int(line) for line in input_data.splitlines()]
