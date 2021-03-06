"""
Test Pandas script to analyze basketball games
"""

import sys

import pandas as pd


class GameAnalyzer:
    """
    Analyze games stats

    Short file descriptor:
    GP - games played
    FGM - field goals made
    FGA - field goals attempted
    3PM - three point made
    PTS - points
    Detailed description - https://en.wikipedia.org/wiki/Basketball_statistics
    """
    dataset_path = 'players_stats_by_season_full_details.csv'

    def __init__(self, dataset_path: str = None):
        stats_dataset = pd.read_csv(dataset_path or self.dataset_path)
        self.dataset = stats_dataset

    def find_most_successful_school(self):
        """Find school with max numbers of success players"""
        max_goals_rec_id = list(self.dataset['FGM'].nlargest(5))
        max_point_rec_id = list(self.dataset['PTS'].nlargest(5))
        max_three_point_rec_id = list(self.dataset['3PM'].nlargest(5))

        result = self.dataset.iloc[max_goals_rec_id + max_point_rec_id
                                   + max_three_point_rec_id]
        result = result.dropna(subset=['high_school'])
        return pd.unique(result['high_school'])

    def find_players_with_max_played_games(self):
        """Find players with maximum games count"""
        mask = self.dataset['GP'] == self.dataset['GP'].max()
        return list(self.dataset[mask]['Player'])

    def find_most_successful_players(self):
        """Find players with max goals made"""
        mask_goals = self.dataset['FGM'] == self.dataset['FGM'].max()
        mask_point = self.dataset['PTS'] == self.dataset['PTS'].max()
        mask_three_point = self.dataset['3PM'] == self.dataset['3PM'].max()
        return list(self.dataset[mask_goals | mask_point | mask_three_point]
                    ['Player'])


if __name__ == '__main__':
    a = GameAnalyzer()
    print("Most successful schools: \n", a.find_most_successful_school())
    print("\nMax games played: \n", a.find_players_with_max_played_games())
    print("\nMost successful players: \n", a.find_most_successful_players())
    sys.exit()
