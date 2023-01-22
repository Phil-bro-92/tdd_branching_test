import unittest
from src.football_results import *


class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.home_win = {"home_score": 2, "away_score": 0}

        self.away_win = {"home_score": 1, "away_score": 3}

        self.draw = {"home_score": 2, "away_score": 2}

        self.final_scores = [
            {"home_score": 2, "away_score": 0},
            {"home_score": 1, "away_score": 3},
            {"home_score": 2, "away_score": 2},
        ]

    # Test we get the right result string for a final score dictionary representing -

    # Home win

    def test_home_win(self):
        self.assertEqual("Home win!", get_result(self.home_win))

    # Away win
    def test_away_win(self):
        self.assertEqual("Away win!", get_result(self.away_win))

    # Draw

    def test_draw(self):
        self.assertEqual("Draw!", get_result(self.draw))

    # Test we get right list of result strings for a list of final score dictionaries.

    def test_correct_final_scores_list(self):
        self.assertEqual(
            ["Home win!", "Away win!", "Draw!"], get_results(self.final_scores)
        )


if __name__ == "__main__":
    unittest.main()
