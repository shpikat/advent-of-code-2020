from day01.common import read_expenses


def main():
    expenses = read_expenses()

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
            print(expenses[little] * expenses[big])
            break
    else:
        print("No pair summing 2020 is detected")



if __name__ == "__main__":
    main()
