import unittest

from day18.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 71 + 51 + 26 + 437 + 12240 + 13632),
        ("puzzle input", puzzle_input, 21022630974613),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 231 + 51 + 46 + 1445 + 669060 + 23340),
        ("puzzle input", puzzle_input, 169899524778212),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
