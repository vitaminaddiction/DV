import pandas as pd


data = pd.read_excel('../sml2.xlsx')
data.set_index('시점', inplace=True)
print(data)

# 컬럼명 배열화
items = data.columns.tolist()
print(items)

startDate_str = "2015-03"
startDate = float(startDate_str.replace('-', '.'))
str_startDate = str(startDate)
print(startDate)

lastDate_str = "2020-02"
lastDate = float(lastDate_str.replace('-', '.'))
str_lastDate = str(lastDate)
print(lastDate)

item = "빵"
print(item)

item2 = ["빵","라면"]
# item2.append 써서 추가하자..
# item2.append()

# 입력값에 따른 dataframe 설정
sml2 = data.loc[str_startDate:str_lastDate, item2]





print(sml2)





