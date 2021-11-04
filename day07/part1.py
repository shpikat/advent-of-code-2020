from collections import defaultdict

from day07.common import read_rules


def solve(filename: str) -> int:
    rules = read_rules(filename)

    index = defaultdict(set)
    for bag, contains in rules:
        for count, contained in contains:
            index[contained].add(bag)

    result = set()
    current_iteration = set(index["shiny gold"])
    while current_iteration:
        result |= current_iteration
        iteration_result = set(contained
                               for bag in current_iteration
                               for contained in index[bag])
        current_iteration = iteration_result - result
    return len(result)
