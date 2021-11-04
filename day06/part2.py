from day06.common import read_answers


def solve(filename: str) -> int:
    answers = read_answers(filename)

    total_count = 0
    for group_answers in answers:
        # we will be needing only 26 bits though
        group_bitset = -1
        for person_answers in group_answers:
            person_bitset = 0
            for single_answer in person_answers:
                person_bitset |= 1 << (ord(single_answer) - ord('a'))
            group_bitset &= person_bitset
        # popcount operation the Python way
        total_count += bin(group_bitset).count('1')

    return total_count
