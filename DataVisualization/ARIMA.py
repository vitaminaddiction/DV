import base64
from io import BytesIO

import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import CalParam

matplotlib.use('Agg')


def arima(startDate, endDate, item):
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    data_val = pd.read_excel('../sml2.xlsx')
    data_val.set_index('시점', inplace=True)

    start_Month = float(startDate.replace('-', '.'))
    # startMonth = "2014-04"

    end_Month = float(endDate.replace('-', '.'))
    # endMonth = "2021-08"

    standard = "생활물가지수"
    i_tem = item

    mylist = []
    mylist.append(standard)
    mylist.append(i_tem)
    # print(mylist)

    # 데이터프레임화
    data2 = data_val.loc[start_Month:end_Month, mylist]
    # data2 = data.loc[labels2,mylist]

    # 각각의 y값 배열화 - json
    standard_value = data2[standard].to_list()
    value1 = standard_value
    i_tem_value = data2[i_tem].to_list()
    value2 = i_tem_value

    # 데이터 불러오기
    data = pd.read_excel('sml99.xlsx')

    # ARIMA 모델 학습
    model = ARIMA(data[item], order=CalParam.calculateParam(item))
    model_fit = model.fit()

    # 2024년 예측
    forecast_steps = 6  # 2024년 1월부터 12월까지 예측
    forecast = model_fit.get_forecast(steps=forecast_steps)

    # 예측 결과 시각화
    plt.figure(figsize=(12, 6))
    # 원래 데이터
    plt.plot(data['시점'], data[item], label='실제 데이터')

    # ARIMA 모델 예측값과 신뢰구간 표시
    forecast_index = pd.date_range(start='2023-11-01', periods=forecast_steps, freq='MS')
    forecast_values = forecast.predicted_mean
    forecast_lower = forecast.conf_int().iloc[:, 0]
    forecast_upper = forecast.conf_int().iloc[:, 1]

    # 예측값과 신뢰구간 시각화
    plt.plot(forecast_index, forecast_values, color='green', label='예측값')
    plt.fill_between(forecast_index, forecast_lower, forecast_upper, color='green', alpha=0.1)

    # 예측 시작점 표시 (빨간색 점선)
    plt.axvline(x=forecast_index[0], color='red', linestyle='--', label='예측 시작점')

    plt.xlabel('시점')
    plt.ylabel(item)
    plt.title(f'2024년 {item} 물가지수 예측')
    plt.legend()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode()

    return img_base64, value1, value2


arima("2013-04", "2013-09", "쌀")
