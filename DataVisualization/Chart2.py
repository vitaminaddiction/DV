import base64

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import matplotlib

matplotlib.use('Agg')


def graph(startMonth, endMonth, item):
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    # 2013.01 ~ 2023.10 연도범위
    data = pd.read_excel('../sml2.xlsx')
    data.set_index('시점', inplace=True)

    start_Month = float(startMonth.replace('-', '.'))
    # startMonth = "2014-04"

    end_Month = float(endMonth.replace('-', '.'))
    # endMonth = "2021-08"

    standard = "생활물가지수"
    i_tem = item

    mylist = []
    mylist.append(standard)
    mylist.append(i_tem)
    # print(mylist)

    labels = generate_months(startMonth, endMonth)
    # '-'를 '.'로 바꾸기
    labels2 = [label.replace('-', '.') for label in labels]
    # print(labels2)

    # 데이터프레임화
    data2 = data.loc[start_Month:end_Month, mylist]
    # data2 = data.loc[labels2,mylist]

    # 각각의 y값 배열화 - json
    standard_value = data2[standard].to_list()
    value1 = standard_value
    i_tem_value = data2[i_tem].to_list()
    value2 = i_tem_value

    # 그래프상의 x좌표 간격 설정 위해서 배열 생성(1단위 크기)
    index_count = len(data2.index)
    print(data2.index)
    index_array = np.arange(1, index_count + 1)
    print(index_array)

    plt.plot(index_array, data2[standard])
    plt.plot(index_array, data2[i_tem])
    plt.xlabel("연도", labelpad=15)

    # 그래프상에서 보여질 눈금배열과 해당 라벨의 배열
    # x_count에 각 년도의 1월을 넣어주자...(나중에)

    arr_x = []
    arr_x.append(2023.01)
    # 하드코딩해서 연도.01월 들을
    # 그래프 x축 라벨로 출력할 예정

    x_count = [1,
               index_count * 1 / 6,
               index_count * 2 / 6,
               index_count * 3 / 6,
               index_count * 4 / 6,
               index_count * 5 / 6,
               index_count * 6 / 6]

    # 임시로 지정
    x_labels = ["0년", "1년", "2년", "3년", "4년", "5년", "6년"]

    plt.xticks(x_count, x_labels)
    plt.ylabel("지수", rotation=0, labelpad=20)
    # plt.show()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    img_base64 = base64.b64encode(img_buffer.read()).decode()

    return img_base64, value1, value2


def graphDefault():
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    startMonth = "2013-01"
    endMonth = "2013-12"
    item = "쌀"

    # 2013.01 ~ 2023.10 연도범위
    data = pd.read_excel('../sml2.xlsx')
    data.set_index('시점', inplace=True)

    start_Month = float(startMonth.replace('-', '.'))
    # startMonth = "2014-04"

    end_Month = float(endMonth.replace('-', '.'))
    # endMonth = "2021-08"

    standard = "생활물가지수"
    i_tem = item

    mylist = []
    mylist.append(standard)
    mylist.append(i_tem)
    # print(mylist)

    labels = generate_months(startMonth, endMonth)
    # '-'를 '.'로 바꾸기
    labels2 = [label.replace('-', '.') for label in labels]
    # print(labels2)

    # 데이터프레임화
    data2 = data.loc[start_Month:end_Month, mylist]
    # data2 = data.loc[labels2,mylist]
    print(data2)

    # 각각의 y값 배열화 - json
    standard_value = data[standard].to_list()
    print(standard_value)
    i_tem_value = data[i_tem].to_list()
    print(i_tem_value)

    # 그래프상의 x좌표 간격 설정 위해서 배열 생성(1단위 크기)
    index_count = len(data2.index)
    print(data2.index)
    index_array = np.arange(1, index_count + 1)
    print(index_array)

    plt.plot(index_array, data2[standard])
    plt.plot(index_array, data2[i_tem])
    plt.xlabel("연도", labelpad=15)

    # 그래프상에서 보여질 눈금배열과 해당 라벨의 배열
    # x_count에 각 년도의 1월을 넣어주자...

    arr_x = []
    arr_x.append(2023.01)

    x_count = [1,
               index_count * 1 / 6,
               index_count * 2 / 6,
               index_count * 3 / 6,
               index_count * 4 / 6,
               index_count * 5 / 6,
               index_count * 6 / 6]
    x_labels = ["0년", "1년", "2년", "3년", "4년", "5년", "6년"]

    plt.xticks(x_count, x_labels)
    plt.ylabel("지수", rotation=0, labelpad=20)
    # plt.show()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return img_buffer


def generate_months(start_month, end_month):
    start_date = datetime.strptime(start_month, '%Y-%m')
    end_date = datetime.strptime(end_month, '%Y-%m')

    months = []
    while start_date <= end_date:
        months.append(start_date.strftime('%Y-%m'))
        start_date += relativedelta(months=1)

    return months
