import ast
from collections import Counter
from sys import exit

import numpy as np
import pandas as pd


class DataParser:
    def __init__(self):
        self._movies = pd.read_csv('../../../movies_metadata.csv')
        # replace with ratings.csv for full calculations,
        # but it takes a lot of time
        self._ratings = pd.read_csv('../../../ratings_small.csv')
        self._user_profile = pd.DataFrame()
        self._movie_profile = pd.DataFrame()

    @staticmethod
    def str_to_snake_case(string):
        snake_case_version = []
        symbols = list(string)

        for symbol in symbols:
            if symbol.isupper():
                snake_case_version.extend(['_', symbol.lower()])
            else:
                snake_case_version.append(symbol)

        return ''.join(snake_case_version)

    @staticmethod
    def retrieve_names_from_genres_collection(items):
        genre_names = []

        for genre in ast.literal_eval(items):
            genre_names.append(genre.get('name'))

        return ', '.join(genre_names)

    @staticmethod
    def timestamp_years_diff(timestamp):
        diff = pd.Timestamp.now() - timestamp
        return diff.days / 365

    @staticmethod
    def average_review_time_diff(timestamps):
        # if zero or one review - there is no average diff
        if len(timestamps) < 2:
            return 0

        timestamps = timestamps.reset_index().sort_values('timestamp')
        diff_count = len(timestamps) - 1
        diff_list = []

        for index in range(1, len(timestamps)):
            prev = timestamps.loc[index - 1]['timestamp']
            current = timestamps.loc[index]['timestamp']
            diff_list.append(current - prev)

        result = pd.Series(diff_list).sum().days / diff_count
        return abs(result)

    @staticmethod
    def get_favourite_genre(data):
        genres = []

        for record in list(data['genres']):
            try:
                genres.extend(record)
            except TypeError:
                pass

        return max(Counter(genres)) if genres else None

    def _prepare_column_names(self):
        def rename(df):
            for column in list(df.columns):
                if column == column.lower():
                    continue

                df.rename(columns={column: self.str_to_snake_case(column)},
                          inplace=True)

        rename(self._movies)
        rename(self._ratings)

        return self

    def _convert_timestamps(self):
        self._ratings['timestamp'] = pd.to_datetime(self._ratings['timestamp'],
                                                    unit='s')
        return self

    def prepare_main_data(self):
        self._prepare_column_names()._convert_timestamps()

    def prepare_movie_profile(self):
        movie_profile = self._movies[['id', 'original_title', 'genres']]
        movie_profile['genres'] = movie_profile['genres'].apply(
            lambda items: self.retrieve_names_from_genres_collection(items))

        # id value sometimes too large, pandas solve it like datetime
        # not best decision, but anyway
        movie_profile['id'] = pd.to_numeric(movie_profile['id'],
                                            errors='coerce')
        movie_profile.dropna(inplace=True)
        movie_profile['id'] = movie_profile['id'].astype(np.int)
        movie_profile.set_index('id', inplace=True)

        movies_rating = self._ratings[['movie_id', 'rating']]
        movies_rating.rename(columns={'movie_id': 'id'}, inplace=True)
        movies_rating = movies_rating.groupby('id').mean()
        self._movie_profile = movie_profile.join(movies_rating)

        return self

    def _get_user_profile_marks_count(self):
        marks_count = self._ratings[['user_id', 'movie_id']]
        marks_count = marks_count.groupby('user_id').count()
        marks_count.rename(columns={'movie_id': 'number_of_marks'},
                           inplace=True)

        marks_count['number_of_marks'] = marks_count['number_of_marks'] \
            .astype(np.int)
        return marks_count

    def _get_user_profile_time_from_first_review(self):
        first_mark = self._ratings[['user_id', 'timestamp']]
        first_mark = first_mark.groupby('user_id').first()
        first_mark.rename(columns={'timestamp': 'years_spend'}, inplace=True)
        first_mark['years_spend'] = first_mark['years_spend'] \
            .apply(lambda x: self.timestamp_years_diff(x))
        return first_mark

    def _get_user_profile_average_mark(self):
        average_mark = self._ratings[['user_id', 'rating']]
        average_mark = average_mark.groupby('user_id').mean()
        average_mark.rename(columns={'rating': 'average_mark'}, inplace=True)
        return average_mark

    def _get_user_profile_average_days_between_marks(self):
        average_mark_time_diff = self._ratings[['user_id', 'timestamp']]
        average_mark_time_diff = average_mark_time_diff.groupby('user_id') \
            .apply(lambda x: self.average_review_time_diff(x))
        average_mark_time_diff.rename('average_time_diff', inplace=True)
        return average_mark_time_diff

    def _get_user_favourite_genres(self):
        favorite_genres = self._ratings[['user_id', 'movie_id', 'rating']]
        favorite_genres = favorite_genres[favorite_genres['rating'] >= 3.8]
        favorite_genres.set_index('movie_id', inplace=True)

        genres = self._movie_profile[['genres']]
        genres['genres'] = genres['genres'].str.split(', ')

        favorite_genres = favorite_genres.join(genres)
        favorite_genres = favorite_genres.groupby('user_id') \
            .apply(self.get_favourite_genre)
        favorite_genres.rename('favourite_genre', inplace=True)

        return favorite_genres

    def prepare_user_profile(self):
        # get user profile
        user = self._ratings[['user_id']]
        user.drop_duplicates(inplace=True)
        user.set_index('user_id', inplace=True)

        user = user.join(self._get_user_profile_marks_count())
        user = user.join(self._get_user_profile_time_from_first_review())
        user = user.join(self._get_user_profile_average_mark())
        user = user.join(self._get_user_profile_average_days_between_marks())
        self._user_profile = user.join(self._get_user_favourite_genres())

        return self

    def export(self):
        if not self._movie_profile.empty:
            self._movie_profile.to_csv('../../../result_movie_profile.csv')

        if not self._user_profile.empty:
            self._user_profile.to_csv('../../../result_user_profile.csv')


if __name__ == '__main__':
    parser = DataParser()
    parser.prepare_main_data()
    parser.prepare_movie_profile().prepare_user_profile()
    parser.export()

    exit()
