import re
from typing import Dict, List, Tuple

MAIN_RULE_INDEX = 0


def part1(input_data: str) -> int:
    raw_rules, messages = read_rules_and_messages(input_data)

    # Didn't want to solve this day using regex, but had to cave in with day 2.
    # The original implementation is still in commit history though.
    regex = get_regex_for_rule(raw_rules, MAIN_RULE_INDEX)
    pattern = re.compile(regex)
    return sum(1 for message in messages if pattern.fullmatch(message))


def get_regex_for_rule(raw_rules: Dict[str, str], rule_index: int) -> str:
    # pre-populate the final characters to simplify the recursion
    memoizer = {
        number: rule[1:-1] for number, rule in raw_rules.items() if rule[0] == rule[-1] == '"'
    }
    return get_regex(raw_rules, memoizer, raw_rules[str(rule_index)])


def get_regex(raw_rules: Dict[str, str], memoizer: Dict[str, str], raw_rule: str) -> str:
    alternative_rules = (
        "".join(
            memoizer.get(atomic_rule) or get_regex(raw_rules, memoizer, raw_rules[atomic_rule])
            for atomic_rule in sequence.split(" ")
        )
        for sequence in raw_rule.split(" | ")
    )
    regex = "(" + "|".join(alternative_rules) + ")"
    memoizer[raw_rule] = regex
    return regex


def part2(input_data: str) -> int:
    raw_rules, messages = read_rules_and_messages(input_data)
    raw_rules["8"] = "42 | 42 8"
    raw_rules["11"] = "42 31 | 42 11 31"

    max_length = max(len(message) for message in messages)

    regex = get_regex_for_rule_capped(raw_rules, MAIN_RULE_INDEX, max_length)
    pattern = re.compile(regex)
    return sum(1 for message in messages if pattern.fullmatch(message))


def get_regex_for_rule_capped(raw_rules: Dict[str, str], rule_index: int, max_length: int) -> str:
    # pre-populate the final characters to simplify the recursion
    memoizer = {
        number: rule[1:-1] for number, rule in raw_rules.items() if rule[0] == rule[-1] == '"'
    }
    return get_regex_capped(raw_rules, memoizer, raw_rules[str(rule_index)], max_length)


def get_regex_capped(
    raw_rules: Dict[str, str],
    memoizer: Dict[str, str],
    raw_rule: str,
    max_length: int,
) -> str:
    alternative_rules = (
        "".join(
            memoizer.get(atomic_rule)
            or get_regex_capped(
                raw_rules,
                memoizer,
                get_next_rule(raw_rules, memoizer, atomic_rule, max_length),
                max_length,
            )
            for atomic_rule in sequence.split(" ")
        )
        for sequence in raw_rule.split(" | ")
    )
    regex = "(" + "|".join(alternative_rules) + ")"
    memoizer[raw_rule] = regex
    return regex


def get_next_rule(
    raw_rules: Dict[str, str], memoizer: Dict[str, str], rule: str, max_length: int
) -> str:
    if rule == "8" and raw_rules["42"] in memoizer:
        regex = "(" + memoizer[raw_rules["42"]] + ")+"
        memoizer[rule] = regex
        return rule
    if rule == "11" and raw_rules["42"] in memoizer and raw_rules["31"] in memoizer:
        regex42 = memoizer[raw_rules["42"]]
        regex31 = memoizer[raw_rules["31"]]
        # I'm already exhausted by this day, I don't want to write the calculation for the length of matching string,
        # let it just be equal to 4!
        n = max_length // 4
        groups = (regex42 + "{" + str(i) + "}" + regex31 + "{" + str(i) + "}" for i in range(1, n))
        regex = "(" + "|".join(groups) + ")"
        memoizer[rule] = regex
        return rule
    return raw_rules[rule]


def read_rules_and_messages(input_data: str) -> Tuple[Dict[str, str], List[str]]:
    rules, messages = input_data.split("\n\n")
    return read_rules_to_list(rules.splitlines()), messages.splitlines()


def read_rules_to_list(lines: List[str]) -> Dict[str, str]:
    rules = {}
    for line in lines:
        i, rule = line.split(": ")
        rules[i] = rule
    return rules
