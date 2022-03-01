import unittest

from day21.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 5),
        ("puzzle input", puzzle_input, 2485),
    )
    test_cases_part2 = (
        ("sample 1", sample1, "mxmxvkd,sqjhc,fvjkl"),
        (
            "puzzle input",
            puzzle_input,
            "bqkndvb,zmb,bmrmhm,snhrpv,vflms,bqtvr,qzkjrtl,rkkrx",
        ),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()
