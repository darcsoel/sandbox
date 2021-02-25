"""
Generate random dates with start date and period
"""

import sys

import pandas as pd

if __name__ == '__main__':
    date_range = pd.period_range('1/1/2020', freq='15d', periods=10)
    print(date_range)

    date_range_diff = pd.DataFrame(date_range, columns=['date']).diff()
    print(date_range_diff)
    sys.exit()
