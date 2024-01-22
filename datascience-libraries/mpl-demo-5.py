# Filling Area on Line Plots
import pandas as pd 
from matplotlib import pyplot as plt

data = pd.read_csv('data1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

plt.plot(ages, py_salaries, label = 'Python')

overall_median = 57287

plt.fill_between(ages, py_salaries, overall_median, 
                 where = (py_salaries > overall_median), 
                 interpolate=True, alpha = 0.2)                                                                    # alpha is opacity

plt.fill_between(ages, py_salaries, overall_median, 
                 where = (py_salaries <= overall_median), 
                 interpolate=True, color='red', alpha = 0.2)  

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()

plt.show()

plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

plt.plot(ages, py_salaries, label = 'Python')

plt.fill_between(ages, py_salaries, dev_salaries, 
                 where = (py_salaries > dev_salaries),
                 interpolate=True, alpha = 0.2, label = 'Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries, 
                 where = (py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha = 0.2, label = 'Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()

plt.show()