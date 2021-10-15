from typing import List, Tuple, Dict


def read_rules_and_messages() -> Tuple[Dict[str, str], List[str]]:
    with open("input", "r") as file:
        rules, messages = file.read().rstrip().split('\n\n')
        return \
            read_rules_to_list(rules.split('\n')), \
            messages.split('\n')


def read_rules_to_list(lines: List[str]) -> Dict[str, str]:
    rules = {}
    for line in lines:
        i, rule = line.split(': ')
        rules[i] = rule
    return rules
