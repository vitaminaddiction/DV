from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import pandas as pd


options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

web = webdriver.Chrome(options=options)

url = 'https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1J20005&vw_cd=MT_ZTITLE&list_id=P2_6&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=K1&path=%25EB%25AC%25BC%25EA%25B0%2580%2520%253E%2520%25EC%2586%258C%25EB%25B9%2584%25EC%259E%2590%25EB%25AC%25BC%25EA%25B0%2580%25EC%25A1%25B0%25EC%2582%25AC%25EC%2583%259D%25ED%2599%259C%25EB%25AC%25BC%25EA%25B0%2580%25EC%25A7%2580%25EC%2588%2598%282020%253D100%29'
web.get(url)

web.switch_to.frame('iframe_rightMenu')
web.implicitly_wait(10)
web.switch_to.frame('iframe_centerMenu')
web.implicitly_wait(10)

Btn_querySetting = web.find_element(By.CSS_SELECTOR, 'button#ico_querySetting.Btn_querySetting')
web.implicitly_wait(10)
Btn_querySetting.click()

tabTimeText = web.find_element(By.ID, 'tabTimeText')
web.implicitly_wait(10)
tabTimeText.click()

select = Select(web.find_element(By.ID, 'selectStrtTimeM'))
web.implicitly_wait(10)
select.select_by_value('202010')

btnSearch = web.find_element(By.ID, 'btnSearch')
web.implicitly_wait(10)
btnSearch.click()
web.implicitly_wait(30)

web.switch_to.default_content()
web.implicitly_wait(10)
web.switch_to.frame('iframe_rightMenu')
web.implicitly_wait(10)
web.switch_to.frame('iframe_centerMenu')
web.implicitly_wait(10)

try:
    web.switch_to.frame('iframe_centerMenu')
    web.implicitly_wait(10)
    html = web.page_source
    web.implicitly_wait(10)
    soup = bs(html, 'html.parser')
    web.implicitly_wait(10)
except Exception as e:
    html = web.page_source
    web.implicitly_wait(10)
    soup = bs(html, 'html.parser')
    web.implicitly_wait(20)
    print(f'{e}, 에러 처리')

itemList = []
timeList = []
valueList = []

items = soup.select('#copyMainTable > tbody > tr > td:nth-of-type(2) > span.last')
web.implicitly_wait(10)
for i in range(len(items)):
    item = items[i].text
    itemList.append(item)

times = soup.select('#mainTableT > thead > tr > th.colHead-first > span:nth-of-type(2)')
for i in range(len(times)):
    time = times[i].text
    timeList.append(time)

values = soup.select('#mainTable > tbody > tr > td.value > span.val')
web.implicitly_wait(10)
for i in range(len(values)):
    value = values[i].text
    valueList.append(value)


chunk_size = len(itemList)
values_chunked = [valueList[i:i + chunk_size] for i in range(0, len(valueList), chunk_size)]

data = []
for i, date in enumerate(timeList):
    row = [date]
    for j, item in enumerate(itemList):
        row.append(values_chunked[i][j])
    data.append(row)

df = pd.DataFrame(data, columns=['시점'] + itemList)
df.set_index('시점', inplace=True)

df.to_excel('data.xlsx')

web.quit()
