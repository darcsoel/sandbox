import sys

import pandas as pd

if __name__ == '__main__':
    pd.options.display.float_format = '{:.1f}'.format
    df = pd.DataFrame({'first': [1.123, 2.123, 3.123]})
    print(df.head())
    sys.exit()
