import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [8, 3, 6, 9, 10]
        self.tie = [3, 4, 7, 7, 1, 2]
        self.two_scores = [3, 6]
        self.one_score = [6]

    # Test latest score (the last thing in the list)
    def test_latest_score_is_10(self):
        self.assertEqual(10, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_highest_score_is_10(self):
        self.assertEqual(10, personal_best(self.scores))

    # Test top three from list of scores
    def test_top_three_are_8_9_10(self):
        self.assertEqual([10, 9, 8], personal_top_three(self.scores))

    # Test ordered from highest tp lowest
    def test_list_ordered_highest_to_lowest(self):
        self.assertEqual([10, 9, 8, 6, 3], sort_high_to_low(self.scores))

    # Test top three when there is a tie
    def test_top_three_when_tie(self):
        self.assertEqual([7, 4, 3], personal_top_three(self.tie))

    # Test top three when there are less than three
    def test_top_three_when_less_than_three(self):
        self.assertEqual([6, 3], personal_top_three(self.two_scores))
    # Test top three when there is only one
    def test_top_three_when_only_one_score(self):
        self.assertEqual([6], personal_top_three(self.one_score))
