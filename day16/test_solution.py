import unittest

from day16.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 71),
        ("puzzle input", puzzle_input, 20013),
    )
    test_cases_part2 = (("puzzle input", puzzle_input, 5977293343129),)

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
