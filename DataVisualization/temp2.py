import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from datetime import datetime

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결


data = pd.read_excel('sample.xlsx')
np_data = np.load('sample.xlsx')

# '시점' 열을 datetime 형식으로 변환
data['시점'] = pd.to_datetime(data['시점'], format='%Y.%m/%d')
# 2014.1/4 가 2014.1.4 로 표기됨.. 수정 필요
data = data.replace('-', None)
# '-' 값 null화


def dv01():
    # 규칙이 딱히 없는 샘플, 선그래프
    plt.figure(figsize=(10,8))

    plt.plot(data['시점'],data['총지수'],label='총지수')
    plt.plot(data['시점'],data['쌀'],label='쌀')
    plt.plot(data['시점'],data['국수'],label='국수')
    plt.plot(data['시점'],data['라면'],label='라면')
    plt.plot(data['시점'],data['빵'],label='빵')
    plt.plot(data['시점'],data['사과'],label='사과')
    plt.plot(data['시점'],data['포도'],label='포도')

    plt.xlabel('시점')
    plt.ylabel('백분율(%)',rotation=90)


    plt.grid(axis='y',color='purple',alpha=0.3)
    plt.legend(loc='upper left')
    # plt.savefig('a.png')
    plt.show()


def dv02():
    # 전반적으로 상승하고 있는 샘플, 점연결그래프

    x = np.data(['시점'])
    y = np.data(['총지수'])
    plt.scatter(x, y)
    plt.plot(x, y)

    plt.figure(figsize=(10, 8))
    plt.plot(data['시점'], data['총지수'], label='총지수')
    plt.plot(data['시점'], data['식품'], label='식품')
    plt.plot(data['시점'], data['쌀'], label='쌀')
    plt.plot(data['시점'], data['두부'], label='두부')
    plt.plot(data['시점'], data['떡'], label='떡')
    plt.plot(data['시점'], data['기타육류가공품'], label='기타육류가공품')
    plt.plot(data['시점'], data['어묵'], label='어묵')

    plt.xlabel('시점')
    plt.ylabel('백분율(%)', rotation=90)

    plt.grid(axis='y', color='purple', alpha=0.3)
    plt.legend(loc='upper left')
    # plt.savefig('a.png')
    plt.show()

dv01()
# dv02()



