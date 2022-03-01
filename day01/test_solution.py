import unittest

from day01.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
1721
979
366
299
675
1456
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 514579),
        ("puzzle input", puzzle_input, 974304),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 241861950),
        ("puzzle input", puzzle_input, 236430480),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
