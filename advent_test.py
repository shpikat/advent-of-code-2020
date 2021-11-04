import os.path
import unittest
from importlib import import_module

import day01
import day02
import day03
import day04
import day05
import day06
import day07
import day08
import day09
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25


class AdventOfCode2020(unittest.TestCase):
    days = (
        (day01, (
            (("sample.txt", 514579), ("input.txt", 974304)),
            (("sample.txt", 241861950), ("input.txt", 236430480)),
        )),
        (day02, (
            (("sample.txt", 2), ("input.txt", 396)),
            (("sample.txt", 1), ("input.txt", 428)),
        )),
        (day03, (
            (("sample.txt", 7), ("input.txt", 156)),
            (("sample.txt", 336), ("input.txt", 3521829480)),
        )),
        (day04, (
            (("sample.txt", 2), ("input.txt", 200)),
            (("sample_invalid.txt", 0), ("sample_valid.txt", 4), ("input.txt", 116)),
        )),
        (day05, (
            (("sample_1.txt", 357), ("sample_2.txt", 567), ("sample_3.txt", 119), ("sample_4.txt", 820),
             ("input.txt", 915)),
            (("input.txt", 699),),
        )),
        (day06, (
            (("sample.txt", 11), ("input.txt", 6782)),
            (("sample.txt", 6), ("input.txt", 3596)),
        )),
        (day07, (
            (("sample.txt", 4), ("input.txt", 302)),
            (("sample.txt", 32), ("sample_2.txt", 126), ("input.txt", 4165)),
        )),
        (day08, (
            (("sample.txt", 5), ("input.txt", 1782)),
            (("sample.txt", 8), ("input.txt", 797)),
        )),
        (day09, (
            (("sample.txt", 127), ("input.txt", 776203571)),
            (("sample.txt", 62), ("input.txt", 104800569)),
        )),
        (day10, (
            (("sample.txt", 35), ("sample_2.txt", 220), ("input.txt", 2775)),
            (("sample.txt", 8), ("sample_2.txt", 19208), ("input.txt", 518344341716992)),
        )),
        (day11, (
            (("sample.txt", 37), ("input.txt", 2472)),
            (("sample.txt", 26), ("input.txt", 2197)),
        )),
        (day12, (
            (("sample.txt", 25), ("input.txt", 2297)),
            (("sample.txt", 286), ("input.txt", 89984)),
        )),
        (day13, (
            (("sample.txt", 295), ("input.txt", 261)),
            (("sample.txt", 1068781), ("sample_2.txt", 3417), ("sample_3.txt", 754018), ("sample_4.txt", 779210),
             ("sample_5.txt", 1261476), ("sample_6.txt", 1202161486), ("input.txt", 807435693182510)),
        )),
        (day14, (
            (("sample_1.txt", 165), ("input.txt", 2346881602152)),
            (("sample_2.txt", 208), ("input.txt", 3885232834169)),
        )),
        (day15, (
            (("sample_1.txt", 436), ("sample_2.txt", 1), ("sample_3.txt", 10), ("sample_4.txt", 27),
             ("sample_5.txt", 78), ("sample_6.txt", 438), ("sample_7.txt", 1836), ("input.txt", 240)),
            (("sample_1.txt", 175594), ("sample_2.txt", 2578), ("sample_3.txt", 3544142), ("sample_4.txt", 261214),
             ("sample_5.txt", 6895259), ("sample_6.txt", 18), ("sample_7.txt", 362), ("input.txt", 505)
             ),
        )),
        (day16, (
            (("sample.txt", 71), ("input.txt", 20013)),
            (("input.txt", 5977293343129),),
        )),
        (day17, (
            (("sample.txt", 112), ("input.txt", 263)),
            (("sample.txt", 848), ("input.txt", 1680)),
        )),
        (day18, (
            (("sample.txt", 71 + 51 + 26 + 437 + 12240 + 13632), ("input.txt", 21022630974613)),
            (("sample.txt", 231 + 51 + 46 + 1445 + 669060 + 23340), ("input.txt", 169899524778212)),
        )),
        (day19, (
            (("sample_1.txt", 2), ("input.txt", 195)),
            (("sample_2.txt", 12), ("input.txt", 309)),
        )),
        (day20, (
            (("sample.txt", 20899048083289), ("input.txt", 108603771107737)),
            (("sample.txt", 273), ("input.txt", 2129)),
        )),
        (day21, (
            (("sample.txt", 5), ("input.txt", 2485)),
            (("sample.txt", "mxmxvkd,sqjhc,fvjkl"),
             ("input.txt", "bqkndvb,zmb,bmrmhm,snhrpv,vflms,bqtvr,qzkjrtl,rkkrx")),
        )),
        (day22, (
            (("sample.txt", 306), ("input.txt", 34005)),
            (("sample.txt", 291), ("input.txt", 32731)),
        )),
        (day23, (
            (("sample.txt", 67384529), ("input.txt", 78569234)),
            (("sample.txt", 149245887792), ("input.txt", 565615814504)),
        )),
        (day24, (
            (("sample.txt", 10), ("input.txt", 375)),
            (("sample.txt", 2208), ("input.txt", 3937)),
        )),
        (day25, (
            (("sample.txt", 14897079), ("input.txt", 17980581)),
        )),
    )

    def test_all(self):
        for module, parts in self.days:
            day = module.__name__
            assert day.startswith("day")
            for i, test_cases in enumerate(parts, start=1):
                assert i in (1, 2)
                part_name = "part" + str(i)
                for filename, answer in test_cases:
                    with self.subTest(day=day, part=part_name, filename=filename):
                        part = import_module(f"{day}.{part_name}")
                        self.assertEqual(part.solve(os.path.join(day, filename)), answer)


if __name__ == '__main__':
    unittest.main()
