import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from io import BytesIO
import numpy as np

matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../sml2.xlsx', index_col=0)

# data.loc['2023.07','쌀']

print(data)
# data = data.drop(columns=['시점'])
# print(data)

print(data)
# 컬럼명 배열화
item = data.columns.tolist()
print(item)


# 날짜 값 두개 입력받음
date1 = data['시점'][0] #string으로 받아야 한다...
# 2023.04
print(date1)
date2 = data['시점'][1]
# 2023.05
print(date2)
year = [date1,date2]


date5 = "2023-04"
date5 = date5.replace('-','.')
print(date5)

print("테스트")
#2023.07
print(data['시점'][1])
# index = data['시점'].index("2023.07")
# print(index)
print("테스트")

# value = data.loc[date5,""]
# print(value)


date3 = '2023.06' #string? datetime? 으로 받을지
print(date3)
date4 = '2023.07'
print(date4)



item1 = '사과' #string으로 받음
value1 = data[item1][0]
print(value1)
value2 = data[item1][1]
print(value2)

# 목록은 어떻게? 스크롤바... 100여개...

x = [1,2]
y = [ value1, value2 ]

plt.figure(figsize=(15, 8))
plt.bar(x, y, width=0.45)

plt.xticks(x, year, rotation=45)
plt.show()

