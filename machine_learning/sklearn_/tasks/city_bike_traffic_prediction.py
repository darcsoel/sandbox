import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar

# airport weather dataset
weather_dataset = pd.read_csv('../../../BicycleWeather.csv')

# how many people across bridge from east to west and vice versa
# information about Siettle fremont bridge
dates_dataset = pd.read_csv('../../../FremontBridge.csv', index_col='Date', parse_dates=True)
dates_dataset = dates_dataset.resample('d', how='sum')  # summary days
dates_dataset['Total'] = dates_dataset.sum(axis=1)

min_year = dates_dataset.index[0].year
max_year = dates_dataset.index[-1].year

holidays = USFederalHolidayCalendar().holidays(str(min_year), str(max_year))
holidays = pd.Series(1, index=holidays, name='Holiday')

dates_dataset = dates_dataset.join(holidays)
dates_dataset['Holiday'].fillna(0, inplace=True)

exit()
