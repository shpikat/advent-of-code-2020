import unittest

from day25.solution import part1
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
5764801
17807724
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 14897079),
        ("puzzle input", puzzle_input, 17980581),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)


if __name__ == "__main__":
    unittest.main()
