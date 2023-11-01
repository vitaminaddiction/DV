import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../sml2.xlsx')

# 컬럼명 배열화
item = data.columns.tolist()
print(item)

# x = [i for i in range(2)]
x = [1,2]
print(x)

y = [j for j in data['사과']]
z = [10,5]
print(y)

# np.set_printoptions(precision=2, suppress=True)
# x = np.arange(6)


plt.figure(figsize=(15,8))
# plt.bar(x, data['사과'], width=1)
plt.bar(x, z, width=0.5,alpha=0.3)
# plt.plot(x, z)

plt.annotate('', xytext=(1, 10), xy=(2, 5), xycoords='data',
        arrowprops=dict(arrowstyle='->', color='red', lw=3))

# 백분율(큰수-작은수)
per = str((5-10)/10*100) + "%"


plt.text(1.5, 8.5, per)

# + 후 나누고 +1~+2 살짝위로

plt.xticks(x,x) # 눈금 지정
plt.show()