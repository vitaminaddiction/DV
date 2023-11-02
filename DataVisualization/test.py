import pandas as pd

data = pd.read_excel('sml0.xlsx')

data.set_index('시점', inplace=True)
print(data)
print(data.index)
date = float(2023.05)
item = "쌀"
value = data.loc[date, item]

print(value)
