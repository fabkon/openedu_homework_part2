from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt_w_tag = 0
cnt_wo_tag = 0
cnt = 0
print(len(soup.find_all('node')))
list_tag = []
for node in soup.find.all('node'):
    if tag in node:
        list_tag.append(tag)

'''for node in soup.find_all('node'): # идем по всем тэгам node
    cnt+=1
    flag = False
    for tag in node:
        flag = True
    if flag:
        cnt_w_tag += 1
    else:
        cnt_wo_tag += 1
'''
print(cnt_wo_tag, cnt_w_tag)
