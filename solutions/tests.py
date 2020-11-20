import unittest
from problem_001 import problem_001, problem_001_faster
from problem_002 import problem_002
from problem_003 import problem_003
from problem_004 import problem_004


class TestProblem001(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_001(10), 23)
        self.assertEqual(problem_001_faster(10), 23)

    def test_answer(self):
        self.assertEqual(problem_001(), 233168)
        self.assertEqual(problem_001_faster(), 233168)


class TestProblem002(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_002(100), 44)

    def test_answer(self):
        self.assertEqual(problem_002(), 4613732)


class TestProblem003(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_003(13195), 29)

    def test_answer(self):
        self.assertEqual(problem_003(), 6857)


class TestProblem004(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_004(2), 9009)

    def test_answer(self):
        self.assertEqual(problem_004(), 906609)


if __name__ == '__main__':
    unittest.main()
