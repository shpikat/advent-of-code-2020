from collections import defaultdict

from day07.common import read_rules


def solve(filename: str) -> int:
    rules = read_rules(filename)

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
    return total_count
