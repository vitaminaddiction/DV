import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import numpy as np


def test2():

        data = pd.read_excel('../sml.xlsx')
        data.set_index('시점',inplace=True)
        print(data)

        startDate_str = "2012-04"
        startDate = float(startDate_str.replace('-','.'))
        print(startDate)
        lastDate_str = "2020-03"
        lastDate = float(lastDate_str.replace('-','.'))
        print(lastDate)
        item = "사과"
        print(item)
        value1 = float(data.loc[startDate,item])
        print(value1)
        value2 = float(data.loc[lastDate,item])
        print(value2)

        x = [1,2] # 조회되는 date 개수를 세어야 함..

        equal = 0
        dataCount = 0
        curDate_str = startDate.str # 변수
        lastDate_str.split('-')

        date = []

        # 카운트를 구하지 말고 원소를 채워넣자..
        while equal > 0 :
                curDate_str.split('-')
                if curDate_str[0]==lastDate_str[0]:#년도 같을때
                        if curDate_str[1]==lastDate_str[1]: #월 같을때, 탈출
                                date.append(curDate_str[0] + '-' + curDate_str[1])
                                equal = 1
                        else: # 월 다를때
                                date.append(curDate_str[0] + '-' + curDate_str[1])
                                curDate_str[1] = str(int(curDate_str[1])+1)+str(0)
                                # 월 하나 올려줌
                else: #년도 다를때
                        date.append(curDate_str[0] + '-' + curDate_str[1])
                        curDate_str[1] = str(int(curDate_str[1]) + 1) + str(0)
                        # 월 하나 올려줌


        # date = [startDate,lastDate]
        value = [value1,value2]

        plt.figure(figsize=(15, 8))
        plt.bar(x, value, width=0.45)

        plt.annotate('', xytext=(1,value1), xy=(2,value2), xycoords='data',
                arrowprops=dict(arrowstyle='->', color='red', lw=3))

        # 백분율(절댓값)
        per = str(round((value[1]-value[0])*100/value[0],1)) + "%"
        # 백분율 텍스트 위치 지정
        plt.text( (x[0]+x[1])/2, ((value[0]+value[1])/2)*1.1, per, fontsize = 25)

        # y축 표기 조정
        gap = max(value) - min(value)
        y = [min(value)-0.2*gap,max(value)+0.2*gap]
        plt.ylim(y)

        plt.xticks(x, date, rotation=45)

        plt.show()



test2()


'''
        # 그래프 그리는 부분
        
        data = pd.read_excel('../sml1.xlsx')
        data.set_index('시점',inplace=True)
        # date1 = "2023-04"
        date1 = float(date1.replace('-','.'))
        # date2 = "2023-08"
        date2 = float(date2.replace('-','.'))
        # item = "사과"
        value1 = float(data.loc[date1,item])
        value2 = float(data.loc[date2,item])

        x = [1,2]
        date = [date1,date2]
        value = [value1,value2]



        plt.figure(figsize=(15, 8))
        plt.bar(x, value, width=0.45)

        plt.annotate('', xytext=(1,value1), xy=(2,value2), xycoords='data',
                arrowprops=dict(arrowstyle='->', color='red', lw=3))

        # 백분율(절댓값)
        per = str(round((value[1]-value[0])*100/value[0],1)) + "%"
        # 백분율 텍스트 위치 지정
        plt.text( (x[0]+x[1])/2, ((value[0]+value[1])/2)*1.1, per)

        plt.xticks(x, date, rotation=45)
        # plt.show()
        
        # 그래프 그리는 부분
        
        
        
# equal = 0
# dataCount = 0
# curDate_str = startDate_str  # 변수
# print(curDate_str)
# print('----')
# ld_split = lastDate_str.split('-')
# print(ld_split[0])
# print(ld_split[1])
# print('----')
# cd_split = curDate_str.split('-')
# print(cd_split[0])
# print(cd_split[1])
# print('----')
#
# date = []
# # date.append(2222.13)
# # date.append(2222.56)
# while equal == 1:
#     if cd_split[0] == ld_split[0]:  # 년도 같을때
#         if cd_split[1] == ld_split[1]:  # 월 같을때, 탈출
#             date.append(cd_split[0] + '-' + cd_split[1])
#             equal = 1
#             print(cd_split[0] + '-' + cd_split[1])
#         else:  # 월 다를때
#             date.append(cd_split[0] + '-' + cd_split[1])
#             cd_split[1] = str(int(cd_split[1]) + 1) + str(0)
#             print(cd_split[0] + '-' + cd_split[1])
#             # 월 하나 올려줌
#     else:  # 년도 다를때
#         date.append(cd_split[0] + '-' + cd_split[1])
#         cd_split[1] = str(int(cd_split[1]) + 1) + str(0)
#         # 월 하나 올려줌
#         print(cd_split[0] + '-' + cd_split[1])
#
# print(date)
# print(len(date))


'''


