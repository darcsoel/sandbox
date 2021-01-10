from sys import exit

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from sklearn.linear_model import LinearRegression
from sklearn.utils import resample


class DataExtractor:
    weather_columns_for_join = ['PRCP', 'Dry day', 'Temp (C)', 'SNOW', 'SNWD',
                                'AWND', 'TMAX', 'TMIN']
    location = 'SEATTLE TACOMA INTERNATIONAL AIRPORT WA US'
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    axis = 23.44
    latitude = 47.61

    def __init__(self):
        self._dates_dataset = pd.read_csv('FremontBridge.csv',
                                          index_col='Date',
                                          parse_dates=True)
        self._min_date = self._dates_dataset.index[0]
        self._max_date = self._dates_dataset.index[-1]

        self._weather_dataset = pd.read_csv('BicycleWeather.csv',
                                            index_col='DATE',
                                            parse_dates=True)

    def _summary_traffic_in_both_directions(self):
        dates_dataset = self._dates_dataset.resample('d').sum()
        dates_dataset['Total'] = dates_dataset.sum(axis=1)
        self._dates_dataset = dates_dataset[['Total']]
        return self

    def __get_holidays(self):
        holiday = USFederalHolidayCalendar().holidays(str(self._min_date.year),
                                                      str(self._max_date.year))
        return pd.Series(1, index=holiday, name='Holiday')

    def _merge_holidays_to_traffic(self):
        self._dates_dataset = self._dates_dataset.join(self.__get_holidays())
        self._dates_dataset['Holiday'].fillna(0, inplace=True)
        return self

    def _add_labels_for_days(self):
        for index, day in enumerate(self.days):
            mask = self._dates_dataset.index.dayofweek == index
            self._dates_dataset[day] = mask.astype(int)
        return self

    def __hours_of_daylight(self, date):
        days = (date - pd.datetime(self._min_date.year,
                                   self._min_date.month,
                                   self._min_date.day)).days
        m = (1. - np.tan(np.radians(self.latitude))
             * np.tan(np.radians(self.axis))) \
            * np.cos(days * 2 * np.pi / 365.25)
        return 24. * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180

    def _merge_daylight_hours_to_days(self):
        h = list(map(self.__hours_of_daylight, self._dates_dataset.index))
        self._dates_dataset['Light_hours'] = h
        return self

    def _prepare_weather(self):
        mask = self._weather_dataset['STATION_NAME'] == self.location
        self._weather_dataset = self._weather_dataset[mask]

        self._weather_dataset['TMAX'] /= 10
        self._weather_dataset['TMIN'] /= 10
        temp = 0.5 * (self._weather_dataset['TMAX'] +
                      self._weather_dataset['TMIN'])
        self._weather_dataset['Temp (C)'] = temp

        self._weather_dataset['PRCP'] /= 254

        mask = self._weather_dataset['PRCP'] == 0
        self._weather_dataset['Dry day'] = mask.astype(int)

        return self

    def _join_weather(self):
        self._prepare_weather()
        prepare_weather = self._weather_dataset[self.weather_columns_for_join]
        self._dates_dataset = self._dates_dataset.join(prepare_weather)
        del self._weather_dataset
        return self

    def _add_counter(self):
        mask = self._dates_dataset.index - self._dates_dataset.index[0]
        self._dates_dataset['Annual'] = mask.days.astype(int)
        return self

    def prepare_dataset(self):
        self._summary_traffic_in_both_directions() \
            ._merge_holidays_to_traffic()._add_labels_for_days() \
            ._merge_daylight_hours_to_days()._join_weather()._add_counter()
        self._dates_dataset.fillna(0, inplace=True)
        return self

    def split_dataset(self):
        result = self._dates_dataset['Total']
        features = self._dates_dataset.drop(columns=['Total'])

        return features, result

    @property
    def dataset(self):
        if not set().issubset(self._dates_dataset.columns):
            raise ValueError('Run prepare_dataset to get full data')

        return self._dates_dataset


if __name__ == '__main__':
    data = DataExtractor().prepare_dataset()
    dataset = data.dataset
    x, y = data.split_dataset()

    np.random.seed(1)
    model = LinearRegression(fit_intercept=False)
    err = np.std([model.fit(*resample(x, y)).coef_ for i in range(1000)], 0)
    dataset['Predicted'] = model.predict(x)

    dataset[['Total', 'Predicted']].plot(alpha=0.5)
    plt.show()

    params = pd.Series(model.coef_, x.columns)
    errors = pd.DataFrame({'params': params.round(0), 'err': err.round(0)})
    print(errors)

    exit()
