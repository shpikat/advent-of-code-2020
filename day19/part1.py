from itertools import product
from typing import List, Dict

from day19.common import read_rules_and_messages

MAIN_RULE_INDEX = 0


def main():
    raw_rules, messages = read_rules_and_messages()

    all_matching_messages = get_matching_messages_for_rule(raw_rules, MAIN_RULE_INDEX)
    print(len(set(all_matching_messages) & set(messages)))


def get_matching_messages_for_rule(raw_rules: Dict[str, str], rule_index: int) -> List[str]:
    # pre-populate the final characters to simplify the recursion
    memoizer = {number: [rule[1:-1]] for number, rule in raw_rules.items() if rule[0] == rule[-1] == '"'}
    return get_messages(raw_rules, memoizer, raw_rules[str(rule_index)])


def get_messages(raw_rules: Dict[str, str], memoizer: Dict[str, List[str]], raw_rule: str) -> List[str]:
    # recursively resolve all the sub-rules
    alternative_sub_rule_messages = (
        (
            memoizer.get(atomic_rule) or get_messages(raw_rules, memoizer, raw_rules[atomic_rule])
            for atomic_rule in sequence.split(' ')
        )
        for sequence in raw_rule.split(' | ')
    )

    # flat map the resolved messages into the matching messages for the current rule
    matching_messages = [
        ''.join(characters)
        for sub_rule_messages in alternative_sub_rule_messages
        for characters in product(*sub_rule_messages)
    ]
    memoizer[raw_rule] = matching_messages
    return matching_messages


if __name__ == "__main__":
    main()
