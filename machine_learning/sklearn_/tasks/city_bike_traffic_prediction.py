import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar


class TrafficPredictor:
    def __init__(self):
        self._dates_dataset = pd.read_csv('../../../FremontBridge.csv', index_col='Date', parse_dates=True)
        # self.weather_dataset = pd.read_csv('../../../BicycleWeather.csv')

    def summary_traffic_in_both_directions(self):
        dates_dataset = self._dates_dataset.resample('d', how='sum')
        dates_dataset['Total'] = dates_dataset.sum(axis=1)
        self._dates_dataset = dates_dataset[['Total']]
        return self

    def _get_min_date(self):
        return self._dates_dataset.index[0].year

    def _get_max_date(self):
        return self._dates_dataset.index[-1].year

    def _get_holidays(self):
        holidays = USFederalHolidayCalendar().holidays(str(self._get_min_date()), str(self._get_max_date()))
        return pd.Series(1, index=holidays, name='Holiday')

    def merge_holidays_to_traffic(self):
        self._dates_dataset = self._dates_dataset.join(self._get_holidays())
        self._dates_dataset['Holiday'].fillna(0, inplace=True)
        return self


if __name__ == '__main__':
    predictor = TrafficPredictor()
    predictor.summary_traffic_in_both_directions().merge_holidays_to_traffic()

    exit()
