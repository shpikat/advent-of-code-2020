import unittest

from day10.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

    sample2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 35),
        ("sample 2", sample2, 220),
        ("puzzle input", puzzle_input, 2775),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 8),
        ("sample 2", sample2, 19208),
        ("puzzle input", puzzle_input, 518344341716992),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
