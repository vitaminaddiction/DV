import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from io import BytesIO
import numpy as np

matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

# data = pd.read_excel('../a.xlsx')
data = pd.read_excel('../sml2.xlsx')

print(data)

# 날짜 값 두개 입력받음

x = ['2023.01','2023.07']
y = [ '100', '50' ]

plt.figure(figsize=(15, 8))
# plt.bar(x, data['사과'], width=0.005)  # width를 0.01로 설정하여 간격을 조절
plt.bar(x, y, width=0.005)  # width를 0.01로 설정하여 간격을 조절

# plt.xticks(x, [f'{year:.2f}' for year in x], rotation=45)  # x 축 눈금 레이블을 2023.04 ~ 2023.09로 설정
plt.xticks(x, [f'{year:.2f}' for year in x], rotation=45)  # x 축 눈금 레이블을 2023.04 ~ 2023.09로 설정
plt.show()

