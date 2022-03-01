import unittest

from day15.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = "0,3,6"
    sample2 = "1,3,2"
    sample3 = "2,1,3"
    sample4 = "1,2,3"
    sample5 = "2,3,1"
    sample6 = "3,2,1"
    sample7 = "3,1,2"

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 436),
        ("sample 2", sample2, 1),
        ("sample 3", sample3, 10),
        ("sample 4", sample4, 27),
        ("sample 5", sample5, 78),
        ("sample 6", sample6, 438),
        ("sample 7", sample7, 1836),
        ("puzzle input", puzzle_input, 240),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 175594),
        ("sample 2", sample2, 2578),
        ("sample 3", sample3, 3544142),
        ("sample 4", sample4, 261214),
        ("sample 5", sample5, 6895259),
        ("sample 6", sample6, 18),
        ("sample 7", sample7, 362),
        ("puzzle input", puzzle_input, 505),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
