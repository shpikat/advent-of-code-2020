import unittest

from day11.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample37", sample1, 37),
        ("puzzle input", puzzle_input, 2472),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 26),
        ("puzzle input", puzzle_input, 2197),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
