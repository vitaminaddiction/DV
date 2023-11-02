import pandas as pd
# DataFrame 생성
df = pd.DataFrame([{"country": "한국", "population": 500},
                   {"country": "미국", "population": 450},
                   {"country": "싱가폴", "population": 705},
                   {"country": "호주", "population": 878},
                   {"country": "베트남", "population": 660},
                   {"country": "대만", "population": 808}])

# 'country' 열이 '한국'인 행에서 'population' 값을 출력
population_korea = df[df['country'] == '한국']['population']
# 결과 출력
print(population_korea)