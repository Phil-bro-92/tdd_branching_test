import unittest

from src.compound_interest import CompoundInterest


class CompoundInterestTest(unittest.TestCase):

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_above_outcome_1(self):
        outcome = CompoundInterest(100, 20, 0.1)
        self.assertEqual(732.81, outcome.calculate_compound_interest())

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_above_outcome_2(self):
        outcome = CompoundInterest(100, 10, 0.06)
        self.assertEqual(181.94, outcome.calculate_compound_interest())

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_above_outcome_3(self):
        outcome = CompoundInterest(100000, 8, 0.05)
        self.assertEqual(149058.55, outcome.calculate_compound_interest())


    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_above_outcome_4(self):
        outcome = CompoundInterest(0, 1, 0.1)
        self.assertEqual(0.00, outcome.calculate_compound_interest())


    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_above_outcome_5(self):
        outcome = CompoundInterest(100, 10, 0)
        self.assertEqual(100.00, outcome.calculate_compound_interest())

    # Extension tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
