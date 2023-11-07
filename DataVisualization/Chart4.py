import base64
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib

matplotlib.use('Agg')


def graph(selected_year, item):
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    data = pd.read_excel('../sml2.xlsx')
    data.set_index('시점', inplace=True)

    select_year = int(selected_year)
    # 봄 : 03, 04, 05 / 여름 : 06, 07, 08 / 가을 : 09, 10, 11 / 겨울 : 12, 01, 02
    # 2020년을 선택했다 : 2020 < selected_year < 2021
    data2 = data.loc[(data.index > select_year) & (data.index < select_year + 1), item]

    # 사계절로 나눠서 data3 담기
    season = ['봄', '여름', '가을', '겨울']
    spring = (data2[select_year + 0.03] + data2[select_year + 0.04] + data2[select_year + 0.05]) / 3
    spr = round(spring, 2)
    summer = (data2[select_year + 0.06] + data2[select_year + 0.07] + data2[select_year + 0.08]) / 3
    sum = round(summer, 2)
    autumn = (data2[select_year + 0.09] + data2[select_year + 0.10] + data2[select_year + 0.11]) / 3
    aut = round(autumn, 2)
    winter = (data2[select_year + 0.12] + data2[select_year + 0.01] + data2[select_year + 0.02]) / 3
    win = round(winter, 2)
    value1 = [spr, sum, aut, win]

    data3 = pd.DataFrame({'계절': season, item: value1})
    data3.set_index('계절', inplace=True)

    # pie 그리기
    explode = [0.05, 0.05, 0.05, 0.05]
    colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    wedgeprops = {'width': 0.8, 'edgecolor': 'w', 'linewidth': 4}

    # 제목 : 컬러 임시지정, 삭제하셔도 됩니다...
    plt.title(item + '의 계절별 평균물가지수', color='blue')
    plt.figure(figsize=(15, 8))
    plt.pie(value1, labels=season, autopct='%.1f%%', startangle=180, counterclock=False,
            colors=colors, explode=explode, wedgeprops=wedgeprops)
    # plt.show()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    img_base64 = base64.b64encode(img_buffer.read()).decode()

    return img_base64, value1


def graphDefault():
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows
    matplotlib.rcParams['font.size'] = 15  # 글자 크기
    matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

    data = pd.read_excel('../sml2.xlsx')
    data.set_index('시점', inplace=True)

    # 연도 선택 : 2020, 품목 : 사과
    selected_year = '2020'  # int인지 string인지 > string 으로 가정
    select_year = int(selected_year)
    # 봄 : 03, 04, 05 / 여름 : 06, 07, 08 / 가을 : 09, 10, 11 / 겨울 : 12, 01, 02
    item = '사과'
    # 2020년을 선택했다 : 2020 < selected_year < 2021
    data2 = data.loc[(data.index > select_year) & (data.index < select_year + 1), item]

    # 사계절로 나눠서 data3 담기
    season = ['봄', '여름', '가을', '겨울']
    spring = (data2[select_year + 0.03] + data2[select_year + 0.04] + data2[select_year + 0.05]) / 3
    spr = round(spring, 2)
    summer = (data2[select_year + 0.06] + data2[select_year + 0.07] + data2[select_year + 0.08]) / 3
    sum = round(summer, 2)
    autumn = (data2[select_year + 0.09] + data2[select_year + 0.10] + data2[select_year + 0.11]) / 3
    aut = round(autumn, 2)
    winter = (data2[select_year + 0.12] + data2[select_year + 0.01] + data2[select_year + 0.02]) / 3
    win = round(winter, 2)
    value1 = [spr, sum, aut, win]
    print(value1)
    data3 = pd.DataFrame({'계절': season, item: value1})
    data3.set_index('계절', inplace=True)

    # pie 그리기
    explode = [0.05, 0.05, 0.05, 0.05]
    colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
    wedgeprops = {'width': 0.8, 'edgecolor': 'w', 'linewidth': 4}

    # 제목 : 컬러 임시지정, 삭제하셔도 됩니다...
    plt.title(item + '의 계절별 평균물가지수', color='blue')
    plt.figure(figsize=(15, 8))
    plt.pie(value1, labels=season, autopct='%.1f%%', startangle=180, counterclock=False,
            colors=colors, explode=explode, wedgeprops=wedgeprops)
    # plt.show()

    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)

    return img_buffer


def generate_months(start_month, end_month):
    start_date = datetime.strptime(start_month, '%Y-%m')
    end_date = datetime.strptime(end_month, '%Y-%m')

    months = []
    while start_date <= end_date:
        months.append(start_date.strftime('%Y-%m'))
        start_date += relativedelta(months=1)

    return months

# 테스트용
# graph(selected_year=2015, item='오이')
