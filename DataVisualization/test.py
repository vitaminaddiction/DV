import pandas as pd


data = pd.read_excel('sample.xlsx')

data.set_index('시점', inplace=True)
print(data)
date = "2014.3/4"
item = "쌀"
value = data.loc[date, item]

print(value)
