import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

data = pd.read_excel('sample1.xlsx')
# print(data)

# total = ['110.80', '111.13', '111.12', '111.20', '112.33', '112.99']
# food = [116.38, 116.85, 117.04, 117.89, 119.89, 120.95]
# cigarette = [100.00, 100.00, 100.00, 100.00, 100.00, 100.00]
# texi = [107.84, 107.84, 110.44, 118.84, 120.19, 121.11]
# delivery = [112.22, 112.22, 112.22, 112.43, 112.45, 112.45]
# gasoline = [118.23, 117.87, 113.88, 113.83, 123.24, 127.14]
# diesel = [128.43, 123.99, 116.90, 116.56, 131.03, 138.69]
#
# x = ['4','5','6','7','8','9']
# y = total
# plt.xlabel('month')
# plt.ylabel('%',rotation=0)
# plt.bar(x, y)
# plt.show()


# plt.bar(x,total)
# plt.bar(x,food)
# plt.bar(x,food)
# plt.bar(x,cigarette)
