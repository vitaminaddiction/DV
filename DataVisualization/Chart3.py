import base64
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import matplotlib

matplotlib.use('Agg')


def graph(startMonth, endMonth):
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    # 2013.01 ~ 2023.10 연도범위
    data = pd.read_excel('../sml2.xlsx')
    data.set_index('시점', inplace=True)

    # '-'를 '.'로 바꾸기
    start_Month = float(startMonth.replace('-', '.'))
    end_Month = float(endMonth.replace('-', '.'))
    labels = generate_months(startMonth, endMonth)


    # 데이터프레임 2
    item = ['오징어','식용유','돼지고기','당근','생활물가지수'] # 임시
    data2 = data.loc[start_Month:end_Month,item]

    # 각각의 y값 배열화 - json
    value1 = data2['오징어'].tolist()
    value2 = data2['식용유'].tolist()
    value3 = data2['돼지고기'].tolist()
    value4 = data2['당근'].tolist()
    value5 = data2['생활물가지수'].tolist()

    # 그래프상의 x좌표 간격 설정 위해서 배열 생성(1단위 크기)
    index_count = len(data2.index)
    index_array = np.arange(1, index_count + 1)

    plt.figure(figsize=(15, 8))

    plt.plot(index_array, value1, marker='o', label='오징어')
    plt.plot(index_array, value2, marker='s', label='식용유')
    plt.plot(index_array, value3, marker='*', label='돼지고기')
    plt.plot(index_array, value4, marker='p', label='당근')
    plt.plot(index_array, value5, marker='D', label='생활물가지수')

    plt.xlabel("시점(개월)", labelpad=15)
    plt.ylabel("지수", rotation=0, labelpad=20)
    plt.legend(loc='upper right')
    plt.title('품목별 물가지수 변화')
    # plt.show()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    img_base64 = base64.b64encode(img_buffer.read()).decode()

    return img_base64, value1, value2, value3, value4, value5

def generate_months(start_month, end_month):
    start_date = datetime.strptime(start_month, '%Y-%m')
    end_date = datetime.strptime(end_month, '%Y-%m')

    months = []
    while start_date <= end_date:
        months.append(start_date.strftime('%Y-%m'))
        start_date += relativedelta(months=1)

    return months


# graph('2016-10','2017-09')