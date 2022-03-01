from typing import List


def part1(input_data: str) -> int:
    answers = read_answers(input_data)

    total_count = 0
    for group_answers in answers:
        bitset = 0
        for person_answers in group_answers:
            for single_answer in person_answers:
                bitset |= 1 << (ord(single_answer) - ord("a"))
        # popcount operation the Python way
        total_count += bin(bitset).count("1")

    return total_count


def part2(input_data: str) -> int:
    answers = read_answers(input_data)

    total_count = 0
    for group_answers in answers:
        # we will be needing only 26 bits though
        group_bitset = -1
        for person_answers in group_answers:
            person_bitset = 0
            for single_answer in person_answers:
                person_bitset |= 1 << (ord(single_answer) - ord("a"))
            group_bitset &= person_bitset
        # popcount operation the Python way
        total_count += bin(group_bitset).count("1")

    return total_count


def read_answers(input_data: str) -> List[List[str]]:
    return [group.rstrip().splitlines() for group in input_data.split("\n\n")]
