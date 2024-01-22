# Pie Chart
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# slices = [60, 40]
# slices = [120, 80, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

# plt.pie(slices, labels=labels, colors = colors, wedgeprops={'edgecolor':'black'})

# plt.title("Pie Chart")
# plt.tight_layout()
# plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels=labels, explode=explode, startangle= 90,
        autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor':'black'})

plt.title("Pie Chart")
plt.tight_layout()
plt.show()