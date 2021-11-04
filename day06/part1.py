from day06.common import read_answers


def solve(filename: str) -> int:
    answers = read_answers(filename)

    total_count = 0
    for group_answers in answers:
        bitset = 0
        for person_answers in group_answers:
            for single_answer in person_answers:
                bitset |= 1 << (ord(single_answer) - ord('a'))
        # popcount operation the Python way
        total_count += bin(bitset).count('1')

    return total_count
