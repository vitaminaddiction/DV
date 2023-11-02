import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# from flask import Flask, request, jsonify, Response
# from flask_cors import CORS
from io import BytesIO
import numpy as np

matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../sml1.xlsx')
data.set_index('시점',inplace=True)
print(data)

# value = data.loc[5,'총지수']
# print(value)
# print('-----')
# value2 = data.loc["2023.09","총지수"]
# print(value2)

date1 = "2023-04"
date1 = date1.replace('-','.')
print(date1)

date2 = "2023-08"
date2 = date2.replace('-','.')
print(date2)

item = "사과"
print(item)
value1 = data.loc["2023.04",item]
print(value1)
print('-------')
value2 = data.loc[date2,item]
print(value2)

# sml1 -> sml3 변환, sml3을 가지고 추출해냄

# 컬럼명 배열화
item = data.columns.tolist()
print(item)

# 날짜 두개 입력받고, 품목 입력받음
# date = date.replace('-','.')






# value1 = data.index[0]
# print(value1)
# value2 = data.index[1]
# print(value2)
# year = [value1,value2]

# 목록은 어떻게? 스크롤바... 100여개...

# x = [1,2]
# y = [ value1, value2 ]
# z = []
# z.append(value1)
# z.append(value2)
# print(z)

# plt.figure(figsize=(15, 8))
# plt.bar(x, y, width=0.45)
#
# plt.annotate('', xytext=(x[0], value1), xy=(x[1], value2), xycoords='data',
#         arrowprops=dict(arrowstyle='->', color='red', lw=3))
#
# # 백분율(큰수-작은수)
# per = str((value2-value1)/10*100) + "%"
#
# plt.text( (x[0]+x[1])/2, (value1+value2)/2*1.1, per)
# # + 후 나누고 +1~+2 살짝위로
#
# plt.xticks(x, y, rotation=45)
# plt.show()

