import unittest
from problem_001 import problem_001, problem_001_faster
from problem_002 import problem_002
from problem_003 import problem_003
from problem_004 import problem_004
from problem_005 import problem_005
from problem_006 import problem_006
from problem_007 import problem_007
from problem_008 import problem_008
from problem_009 import problem_009
from problem_010 import problem_010
from problem_011 import problem_011
from problem_012 import problem_012
from problem_013 import problem_013
from problem_014 import problem_014
from problem_015 import problem_015
from problem_016 import problem_016
from problem_017 import problem_017
from problem_020 import problem_020
from problem_021 import problem_021
from problem_022 import problem_022
from problem_023 import problem_023
from problem_025 import problem_025
from problem_027 import problem_027


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


class TestProblem005(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_005(10), 2520)

    def test_answer(self):
        self.assertEqual(problem_005(), 232792560)


class TestProblem006(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_006(10), 2640)

    def test_answer(self):
        self.assertEqual(problem_006(), 25164150)


class TestProblem007(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_007(6), 13)

    def test_answer(self):
        self.assertEqual(problem_007(), 104743)


class TestProblem008(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_008(series=4), 5832)

    def test_answer(self):
        self.assertEqual(problem_008(), 23514624000)


class TestProblem009(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_009(), 31875000)


class TestProblem010(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_010(10), 17)

    def test_answer(self):
        self.assertEqual(problem_010(), 142913828922)


class TestProblem011(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_011(), 70600674)


class TestProblem012(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_012(5), 28)

    def test_answer(self):
        self.assertEqual(problem_012(), 76576500)


class TestProblem013(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_013(), 5537376230)


class TestProblem014(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_014(), 837799)


class TestProblem015(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_015(2), 6)

    def test_answer(self):
        self.assertEqual(problem_015(), 137846528820)


class TestProblem016(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_016(15), 26)

    def test_answer(self):
        self.assertEqual(problem_016(), 1366)


class TestProblem017(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_017(5), 19)

    def test_answer(self):
        self.assertEqual(problem_017(), 21124)


class TestProblem020(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_020(10), 27)

    def test_answer(self):
        self.assertEqual(problem_020(), 648)


class TestProblem021(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_021(), 31626)


class TestProblem022(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_022(), 871198282)


class TestProblem023(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(problem_023(12), sum(range(12)))

    def test_example_2(self):
        self.assertEqual(problem_023(25), sum(range(25)) - 24)

    def test_answer(self):
        self.assertEqual(problem_023(), 4179871)


class TestProblem025(unittest.TestCase):

    def test_example(self):
        self.assertEqual(problem_025(3), 12)

    def test_answer(self):
        self.assertEqual(problem_025(), 4782)


class TestProblem027(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(problem_027(), -59231)


if __name__ == '__main__':
    unittest.main()
