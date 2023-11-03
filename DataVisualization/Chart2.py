import base64

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from io import BytesIO

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta



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
    data2 = data.loc[start_Month:end_Month,mylist]
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

    plt.plot(index_array,data2[standard])
    plt.plot(index_array, data2[i_tem])
    plt.xlabel("연도",labelpad=15)

    # 그래프상에서 보여질 눈금배열과 해당 라벨의 배열
    # x_count에 각 년도의 1월을 넣어주자...

    arr_x = []
    arr_x.append(2023.01)




    x_count = [1,
               index_count*1/6,
               index_count*2/6,
               index_count*3/6,
               index_count*4/6,
               index_count*5/6,
               index_count*6/6]
    x_labels = ["0년","1년","2년","3년","4년","5년","6년"]

    plt.xticks(x_count,x_labels)
    plt.ylabel("지수",rotation=0,labelpad=20)
    plt.show()

    # plt.plot(data2.index, )

    # x = [1, 2]
    # date = [startMonth, endMonth]
    # value = [value1, value2]
    #
    # plt.figure(figsize=(15, 8))
    # plt.bar(x, value, width=0.45, color='green')
    #
    # plt.annotate('', xytext=(1, value1), xy=(2, value2), xycoords='data',
    #              arrowprops=dict(arrowstyle='->', color='red', lw=3))
    #
    # # 백분율(절댓값)
    # per = str(round((value[1] - value[0]) * 100 / value[0], 1)) + "%"
    # # 백분율 텍스트 위치 지정
    # plt.text((x[0] + x[1]) / 2, ((value[0] + value[1]) / 2) * 1.1, per)
    #
    # y = [80, 150]
    # plt.ylim(y)
    #
    # plt.xticks(x, date, rotation=45)
    # plt.show()
    #
    # img_buffer = BytesIO()
    # plt.savefig(img_buffer, format="png")
    # img_buffer.seek(0)
    #
    # img_base64 = base64.b64encode(img_buffer.read()).decode()

    # return img_base64, value1, value2
    return "test"

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
    plt.show()

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

