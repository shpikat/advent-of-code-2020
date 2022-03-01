import unittest

from day05.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = "FBFBBFFRLR"

    sample2 = "BFFFBBFRRR"

    sample3 = "FFFBBBFRRR"

    sample4 = "BBFFBBFRLL"

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 357),
        ("sample 2", sample2, 567),
        ("sample 3", sample3, 119),
        ("sample 4", sample4, 820),
        ("puzzle input", puzzle_input, 915),
    )
    test_cases_part2 = (("puzzle input", puzzle_input, 699),)

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
