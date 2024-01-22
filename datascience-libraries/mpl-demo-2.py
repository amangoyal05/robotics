# Bar Charts
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes - width, dev_y, width= width, color='#444444', label = 'All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y,  width= width, color='#008fd5', label = 'Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 83640]

plt.bar(x_indexes + width, js_dev_y, width= width, color='#e5ae38', label = 'Javscript')

plt.xticks(ticks = x_indexes, labels = ages_x)
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

# Adding Legends
plt.legend()

# Adjusting padding
plt.tight_layout()

plt.show()


# Plotting data from a CSV file
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

lang_counter = Counter()

for response in lang_responses:
    lang_counter.update(response.split(';'))

languages = []
popularity = []

for item in lang_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()