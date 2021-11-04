import re
from typing import Dict

from day19.common import read_rules_and_messages

MAIN_RULE_INDEX = 0


def solve(filename: str) -> int:
    raw_rules, messages = read_rules_and_messages(filename)

    # Didn't want to solve this day using regex, but had to cave in with day 2.
    # The original implementation is still in commit history though.
    regex = get_regex_for_rule(raw_rules, MAIN_RULE_INDEX)
    pattern = re.compile(regex)
    return sum(1 for message in messages if pattern.fullmatch(message))


def get_regex_for_rule(raw_rules: Dict[str, str], rule_index: int) -> str:
    # pre-populate the final characters to simplify the recursion
    memoizer = {number: rule[1:-1] for number, rule in raw_rules.items() if rule[0] == rule[-1] == '"'}
    return get_regex(raw_rules, memoizer, raw_rules[str(rule_index)])


def get_regex(raw_rules: Dict[str, str], memoizer: Dict[str, str], raw_rule: str) -> str:
    alternative_rules = (
        ''.join(
            memoizer.get(atomic_rule) or get_regex(raw_rules, memoizer, raw_rules[atomic_rule])
            for atomic_rule in sequence.split(' ')
        )
        for sequence in raw_rule.split(' | ')
    )
    regex = '(' + '|'.join(alternative_rules) + ')'
    memoizer[raw_rule] = regex
    return regex
