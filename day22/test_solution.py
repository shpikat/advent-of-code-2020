import unittest

from day22.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 306),
        ("puzzle input", puzzle_input, 34005),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 291),
        ("puzzle input", puzzle_input, 32731),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
