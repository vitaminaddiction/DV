import base64

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
from flask import jsonify


def graph2(startDate, lastDate, item):
    # 기간 고정(5년), 선택 품목 출력, 점선그래프
    # 생활물가지수 상시 출력


    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    data = pd.read_excel('../sml1.xlsx')
    data.set_index('시점', inplace=True)
    # date1 = "2023-04"
    startDate = float(startDate.replace('-', '.'))
    # date2 = "2023-08"
    lastDate = float(lastDate.replace('-', '.'))
    # item = "사과"
    value1 = float(data.loc[startDate, item])
    value2 = float(data.loc[lastDate, item])

    x = [1, 2]
    date = [startDate, lastDate]
    value = [value1, value2]

    plt.figure(figsize=(15, 8))
    plt.bar(x, value, width=0.45)

    plt.annotate('', xytext=(1, value1), xy=(2, value2), xycoords='data',
                 arrowprops=dict(arrowstyle='->', color='red', lw=3))

    # 백분율(절댓값)
    per = str(round((value[1] - value[0]) * 100 / value[0], 1)) + "%"
    # 백분율 텍스트 위치 지정
    plt.text((x[0] + x[1]) / 2, ((value[0] + value[1]) / 2) * 1.1, per)
    # y축 표기 조정
    gap = max(value) - min(value)
    y = [min(value) - 0.2 * gap, max(value) + 0.2 * gap]
    plt.ylim(y)

    plt.xticks(x, date, rotation=45)
    # plt.show()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    img_base64 = base64.b64encode(img_buffer.read()).decode()


    return img_base64, value1, value2