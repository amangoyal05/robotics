# Time series
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-v0_8')

dates = [
    datetime(2024, 1, 24),
    datetime(2024, 1, 25),
    datetime(2024, 1, 26),
    datetime(2024, 1, 27),
    datetime(2024, 1, 28),
    datetime(2024, 1, 29),
    datetime(2024, 1, 30),
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='solid')

# gcf - Get Current Figure. Formats the dates label on the x axis.
plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d, %Y')

# gca - Get Current Axis
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()

data = pd.read_csv('data3.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle = 'solid')

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.show()