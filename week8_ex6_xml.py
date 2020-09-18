from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml


list_tag = []
ways={}
for way in soup.find_all('way'): # идем по всем тэгам way
    for nd in way('nd'):
        ways[way['id']] = ways.get(way['id'], 0) + 1 #счетчик через get без if
temp_list=[]
for key in ways:
    temp_list.append([ways[key], key])

max_way = max(temp_list)

print(max_way[1])