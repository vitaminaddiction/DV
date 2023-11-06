import matplotlib.pyplot as plt
import pandas as pd  # pandas 라는 모듈을 pd 라는 별칭(alias)으로 사용
import numpy as np  # numpy 라는 모듈을 np 라는 별명(alias)으로 사용
import warnings
warnings.simplefilter("ignore")

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("../sml1.xlsx")
extracted_data = data.iloc[0:3] #[]괄호 안쪽은 0번째 부터 3번째 (ex 0,1,2 뒤에 숫자만큼만 나옴) 자료만 추출 하는 것
print(extracted_data)

# 도시가스(좀 미비), 국산쇠고기, 수입쇠고기,돼지고기, 고등어, (사과, 수박, 바나나, 배추, 시금치, 당근 , 오이, 호박 , 양파 , 파, 풋고추(야채류 다추천))

#data.plot(figsize=(20,5))
plt.axis('equal')
w = {"edgecolor": "black", "linewidth":5, "width":0.5}
wed={"width":0.7} # 원형 그래프 안쪽 구멍 크기 숫자 클수록 비워 지는 구멍 크기는 작아짐
plt.pie(extracted_data['전기료'], labels=extracted_data['시점'], wedgeprops=wed, startangle=90, autopct='%1.1f%%')
plt.title('분기별 전기 사용량')
plt.show()