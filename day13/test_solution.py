import unittest

from day13.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
939
7,13,x,x,59,x,31,19
"""

    sample2 = """
0
17,x,13,19
"""

    sample3 = """
0
67,7,59,61
"""

    sample4 = """
0
67,x,7,59,61
"""

    sample5 = """
0
67,7,x,59,61
"""

    sample6 = """
0
1789,37,47,1889
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 295),
        ("puzzle input", puzzle_input, 261),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 1068781),
        ("sample 2", sample2, 3417),
        ("sample 3", sample3, 754018),
        ("sample 4", sample4, 779210),
        ("sample 5", sample5, 1261476),
        ("sample 6", sample6, 1202161486),
        ("puzzle input", puzzle_input, 807435693182510),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
