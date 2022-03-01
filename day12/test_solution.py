import unittest

from day12.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
F10
N3
F7
R90
F11
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 25),
        ("puzzle input", puzzle_input, 2297),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 286),
        ("puzzle input", puzzle_input, 89984),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
