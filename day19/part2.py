import re
from typing import Dict

from day19.common import read_rules_and_messages

MAIN_RULE_INDEX = 0


def main():
    raw_rules, messages = read_rules_and_messages()
    raw_rules["8"] = "42 | 42 8"
    raw_rules["11"] = "42 31 | 42 11 31"

    max_length = max(len(message) for message in messages)

    regex = get_regex_for_rule(raw_rules, MAIN_RULE_INDEX, max_length)
    pattern = re.compile(regex)
    print(sum(1 for message in messages if pattern.fullmatch(message)))


def get_regex_for_rule(raw_rules: Dict[str, str], rule_index: int, max_length: int) -> str:
    # pre-populate the final characters to simplify the recursion
    memoizer = {number: rule[1:-1] for number, rule in raw_rules.items() if rule[0] == rule[-1] == '"'}
    return get_regex(raw_rules, memoizer, raw_rules[str(rule_index)], max_length)


def get_regex(raw_rules: Dict[str, str], memoizer: Dict[str, str], raw_rule: str, max_length: int) -> str:
    alternative_rules = (
        ''.join(
            memoizer.get(atomic_rule)
            or get_regex(
                raw_rules,
                memoizer,
                get_next_rule(raw_rules, memoizer, atomic_rule, max_length),
                max_length)
            for atomic_rule in sequence.split(' ')
        )
        for sequence in raw_rule.split(' | ')
    )
    regex = '(' + '|'.join(alternative_rules) + ')'
    memoizer[raw_rule] = regex
    return regex


def get_next_rule(raw_rules: Dict[str, str], memoizer: Dict[str, str], rule: str, max_length: int) -> str:
    if rule == "8" and raw_rules["42"] in memoizer:
        regex = '(' + memoizer[raw_rules["42"]] + ')+'
        memoizer[rule] = regex
        return rule
    if rule == "11" and raw_rules["42"] in memoizer and raw_rules["31"] in memoizer:
        regex42 = memoizer[raw_rules["42"]]
        regex31 = memoizer[raw_rules["31"]]
        # I'm already exhausted by this day, I don't want to write the calculation for the length of matching string,
        # let it just be equal to 4!
        n = max_length // 4
        regex = '(' + '|'.join(regex42 + '{' + str(i) + '}' + regex31 + '{' + str(i) + '}' for i in range(1, n)) + ')'
        memoizer[rule] = regex
        return rule
    return raw_rules[rule]


if __name__ == "__main__":
    main()
