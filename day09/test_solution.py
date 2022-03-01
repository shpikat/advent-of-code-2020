import unittest

from day09.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 5, 127),
        ("puzzle input", puzzle_input, 25, 776203571),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 5, 62),
        ("puzzle input", puzzle_input, 25, 104800569),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)

    def run_tests_for_part(self, part, test_cases):
        for test_name, input_data, preamble_size, answer in test_cases:
            with self.subTest(test_name):
                self.assertEqual(part(input_data.strip(), preamble_size), answer)


if __name__ == "__main__":
    unittest.main()
