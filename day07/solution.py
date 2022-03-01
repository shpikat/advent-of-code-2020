import re
from collections import defaultdict
from typing import List, Tuple


def part1(input_data: str) -> int:
    rules = read_rules(input_data)

    index = defaultdict(set)
    for bag, contains in rules:
        for count, contained in contains:
            index[contained].add(bag)

    result = set()
    current_iteration = set(index["shiny gold"])
    while current_iteration:
        result |= current_iteration
        iteration_result = set(contained for bag in current_iteration for contained in index[bag])
        current_iteration = iteration_result - result
    return len(result)


def part2(input_data: str) -> int:
    rules = read_rules(input_data)

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


parser_bag = re.compile(r"(\w+ \w+) bags contain ")
parser_contains = re.compile(r"(\d+) (\w+ \w+) bags?(, )?")


def read_rules(input_data: str) -> List[Tuple[str, List[Tuple[int, str]]]]:
    return [parse(rule.strip()) for rule in input_data.splitlines()]


def parse(rule: str) -> Tuple[str, List[Tuple[int, str]]]:
    bag = parser_bag.match(rule).group(1)
    contains = [
        (int(match.group(1)), match.group(2)) for match in parser_contains.finditer(rule, len(bag))
    ]
    return bag, contains
