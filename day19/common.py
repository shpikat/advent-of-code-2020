from typing import List, Tuple


def read_rules_and_messages() -> Tuple[List[str], List[str]]:
    with open("input", "r") as file:
        rules, messages = file.read().rstrip().split('\n\n')
        return \
            read_rules_to_list(rules.split('\n')), \
            messages.split('\n')


def read_rules_to_list(lines: List[str]) -> List[str]:
    rules = [''] * len(lines)
    for line in lines:
        i, rule = line.split(': ')
        rules[int(i)] = rule
    return rules
