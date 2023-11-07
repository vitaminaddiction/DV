import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima.model import ARIMA
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

# 데이터 불러오기
data = pd.read_excel('sml99.xlsx')
print(data)
# 시점을 datetime 형식으로 변환
# data['시점'] = pd.to_datetime(data['시점'].astype(str).str.replace('.', '-') + '-01')

# 인덱스 설정
# data.set_index('시점', inplace=True)

train = data[0:120]
test = data[120:]

print(train['쌀'])
print(train['시점'])

diff_1 = train['쌀'].diff().dropna()
diff_2 = diff_1.diff().dropna()

model = ARIMA(train['쌀'], order=(1, 1, 0))
model_fit = model.fit()
print(model_fit.summary())

# 2024년 예측
future_steps = 12  # 2024년 1월부터 12월까지 총 12개월 예측
forecast = model_fit.get_forecast(steps=future_steps)



# 예측 결과 시각화
plt.figure(figsize=(12, 6))
plt.plot(data['시점'], data['쌀'], label='실제 데이터')
plt.plot(pd.date_range(start='2023-11-01', periods=future_steps, freq='MS'), forecast.predicted_mean, label='2024년 예측')
plt.fill_between(pd.date_range(start='2023-11-01', periods=future_steps, freq='MS'),
                 forecast.conf_int().iloc[:, 0],
                 forecast.conf_int().iloc[:, 1], color='gray', alpha=0.2)
plt.xlabel('시점')
plt.ylabel('쌀')
plt.title('ARIMA 모델을 사용한 생활물가지수 예측')
plt.legend()
plt.show()

# # ARIMA 모델 학습
# model = ARIMA(data['쌀'], order=(2, 2, 1))  # ARIMA(p,d,q) 모델, 여기서는 p=5, d=1, q=0으로 설정했습니다.
# model_fit = model.fit()
#
# # 모델 요약 정보 확인
# print(model_fit.summary())
#
# # 2024년 예측
# future_steps = 12  # 2024년 1월부터 12월까지 총 12개월 예측
# forecast = model_fit.get_forecast(steps=future_steps)
#
# # 예측 결과 시각화
# plt.figure(figsize=(12, 6))
# plt.plot(data.index, data['쌀'], label='실제 데이터')
# plt.plot(pd.date_range(start='2023-11-01', periods=future_steps, freq='MS'), forecast.predicted_mean, label='2024년 예측')
# plt.fill_between(pd.date_range(start='2023-11-01', periods=future_steps, freq='MS'),
#                  forecast.conf_int().iloc[:, 0],
#                  forecast.conf_int().iloc[:, 1], color='gray', alpha=0.2)
# plt.xlabel('시점')
# plt.ylabel('생활물가지수')
# plt.title('ARIMA 모델을 사용한 생활물가지수 예측')
# plt.legend()
# plt.show()
