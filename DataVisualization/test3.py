import pandas as pd


data = pd.read_excel('../sml.xlsx')
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
sml3 = data.loc[str_startDate:str_lastDate, item2]

bread = sml3.loc['빵']
print(bread)


# # item = "사과"
# value1 = float(data.loc[date1, item])
# value2 = float(data.loc[date2, item])
#
# x = [1, 2]
# date = [date1, date2]
# value = [value1, value2]
#
# plt.figure(figsize=(15, 8))
# plt.bar(x, value, width=0.45)
#
# plt.annotate('', xytext=(1, value1), xy=(2, value2), xycoords='data',
#              arrowprops=dict(arrowstyle='->', color='red', lw=3))
#
# # 백분율(절댓값)
# per = str(round((value[1] - value[0]) * 100 / value[0], 1)) + "%"
# # 백분율 텍스트 위치 지정
# plt.text((x[0] + x[1]) / 2, ((value[0] + value[1]) / 2) * 1.1, per)
#
# plt.xticks(x, date, rotation=45)
# # plt.show()
#
#
#
#
#
# print(sml3)





