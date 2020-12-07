from collections import defaultdict

from day07.common import read_rules


def main():
    rules = read_rules()

    rules = dict(rules)

    total_count = 0
    next_iteration = {"shiny gold": 1}
    while next_iteration:
        current_iteration = next_iteration.items()
        next_iteration = defaultdict(int)
        for bag, bag_count in current_iteration:
            for next_bag_count, next_bag in rules[bag]:
                next_iteration[next_bag] += bag_count * next_bag_count
        total_count += sum(next_iteration.values())
    print(total_count)


if __name__ == "__main__":
    main()
