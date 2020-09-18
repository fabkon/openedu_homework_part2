import xmltodict

fin = open('map.osm', 'r', encoding='utf8')
xmltext = fin.read()
fin.close()
xml = xmltodict.parse(xmltext)

for plant in xml['CATALOG']['PLANT']:
    for key in plant:
        print(key, plant[key])
    print('---')