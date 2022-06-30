# Course on Python and Statistics for Financial Analysis 
# Source of course is found here: https://www.coursera.org/learn/python-statistics-financial-analysis

import pandas as pd
import matplotlib.pyplot as plt


fb = pd.read_csv('facebook.csv', index_col=0)
ms = pd.read_csv('microsoft.csv', index_col=0)

print(fb.head())

# we can slice dataframe by either label (.loc) or by position (.iloc)
print(fb.loc['2022-01-01':'2022-12-31', 'Close'])

# fb.loc['2022-01-01':'2022-12-31', 'Close'].plot()
fb['Close'].plot()
x = fb.loc['2022-01-01':'2022-12-31', 'Close']
print("hello world")
plt.plot(x)
