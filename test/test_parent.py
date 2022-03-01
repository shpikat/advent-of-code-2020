import pathlib
import time
import unittest


def read_text_file(module: str, filename: str) -> str:
    with open(pathlib.Path(module).parent.joinpath(filename), "r") as file:
        return file.read()


class ParentTestCase(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f"({round(elapsed, 3)}s)", flush=True)

    def run_tests_for_part(self, part, test_cases):
        for test_name, input_data, answer in test_cases:
            with self.subTest(test_name):
                self.assertEqual(part(input_data.strip()), answer)
