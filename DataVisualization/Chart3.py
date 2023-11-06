import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 불러오기
df = pd.read_excel("../sml1.xlsx")
plt.rcParams['font.family'] = 'Malgun Gothic'

# 엑셀 파일의 필요한 열 선택
col1 = df['쌀']  # 열1의 이름을 지정하세요
col2 = df['국수']  # 열2의 이름을 지정하세요
col3 = df['라면']  # 열3의 이름을 지정하세요
col4 = df['두부']  # 열4의 이름을 지정하세요

# 그래프 생성
plt.plot(col1, marker='o', label='쌀')
plt.plot(col2, marker='s', label='국수')
plt.plot(col3, marker='^', label='라면')
plt.plot(col4, marker='*', label='두부')
#plt.plot(col4, marker='<', label='') #품목 최대 5개만 선택 가능하게 되면 좋겟어요,,

# X, Y 축 레이블 설정
plt.xlabel('각 연도별')
plt.ylabel('물가')
#plt.xticks('시점')

# 그래프 제목 설정
plt.title('startDate 에서 endDate 까지 품목별 물가 변화')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()