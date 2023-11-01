import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from datetime import datetime

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

data = pd.read_excel('sample2.xlsx')
data = data.replace('-', None)
df = pd.DataFrame(data)

x = data['시점']
print(x)
y = data['식품']
print(y)


# if data['시점']=='2022.12':
#     print(data['식품'])

# np_data = np.load('sample2.xlsx')

# '시점' 열을 datetime 형식으로 변환
# data['시점'] = pd.to_datetime(data['시점'], format='%Y.%m/%d')
# data['시점'] = pd.to_datetime(data['시점'], format='%Y.%m')
# 2014.1/4 가 2014.1.4 로 표기됨.. 수정 필요




# '-' 값 null화


def dv01():
    # 막대그래프, 특정 기간 A->B n% 상승, 하락
    # a = input('A년부터 B년까지 C품목 : A,B,C 형식으로 입력해주세요')
    # b = a.split(',')
    # first_year = int(b[0])
    # last_year = int(b[1])
    # target = str(b[2])

    # plt.figure(figsize=(10, 8))
    # '2023.05' 시점의 데이터 추출


    # data_2022_11 = data[data['시점'] == '2022.11']
    # data_2023_09 = data[data['시점'] == '2023.09']

    # filtered_data = data[data['시점'].isin(['2022.11', '2023.09'])]

    plt.bar(data['시점'], data['사과'], label='사과')
    # plt.scatter(data['시점'], data['사과'], label='사과')

    # plt.xlabel('시점')
    # plt.ylabel('백분율(%)', rotation=90)

    # plt.grid(axis='y', color='purple', alpha=0.3)
    # plt.legend(loc='upper left')
    # plt.savefig('a.png')
    plt.show()

    # '시점' 열의 값이 '2022.11' 또는 '2023.09'인 행을 추출
    # filtered_data = data[data['시점'].isin(['2022.11', '2023.09'])]
    # df[df['시점']=='2022.11'&[df['생활물가지수']]]

    tar1 = df[df['시점'] == '2022.11']['사과']
    print(tar1)

    # 결과 출력
    # print(data['시점'])


def dv02():
    # 기간 고정(ex:5년, 연도로 끊음), 해놓고 선택한 해당 상품만 출력, 점그래프

    x = np.data(['시점'])
    y = np.data(['총지수'])
    plt.scatter(x, y)
    plt.plot(x, y)

    plt.figure(figsize=(10, 8))
    plt.plot(data['시점'], data['총지수'], label='총지수')
    # plt.plot(data['시점'], data['식품'], label='식품')
    # plt.plot(data['시점'], data['쌀'], label='쌀')
    # plt.plot(data['시점'], data['두부'], label='두부')
    # plt.plot(data['시점'], data['떡'], label='떡')
    # plt.plot(data['시점'], data['기타육류가공품'], label='기타육류가공품')
    # plt.plot(data['시점'], data['어묵'], label='어묵')

    plt.xlabel('시점')
    plt.ylabel('백분율(%)', rotation=90)

    plt.grid(axis='y', color='purple', alpha=0.3)
    plt.legend(loc='upper left')
    # plt.savefig('a.png')
    plt.show()


def dv03():
    # 해당 기간 내(1년? 분기?)에 제일 많이 오른 품목(상승률,하락률) >> 점연결그래프
    # 결과 :: 어떤 품목이 가장 올랐다..!

    plt.show()


def dv04():
    # 해당 년도에(계절에) 해당 카테고리가 어떻게 분포돼있나? ~~ >> 원형그래프
    # ex : 1년치 비교 - ex : 가스 : 봄/여름/가을/겨울
    # 년/분기별 비교 - ex : 사과 : 23봄/22봄/21봄/20봄

    plt.show()


dv01()
# dv02()
# dv03()
# dv04()
