from typing import Dict, List, Tuple


def read_rules_and_messages(filename: str) -> Tuple[Dict[str, str], List[str]]:
    with open(filename, "r") as file:
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
