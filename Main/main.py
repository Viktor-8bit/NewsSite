import unicodedata
import requests
from bs4 import BeautifulSoup as bs
import sqlite3
import time
import random


con = sqlite3.connect("C:\\Users\\512\\Desktop\\ksp\\NewsSite\\Main\\db.sqlite3")
cur = con.cursor()

#
#
#
# парсим сегодня 891107, 891207 100 значений
#
#
#

for i in range(891107, 891207): # 36 есть 

    URL_TEMPLATE = "https://www.interfax.ru/world/" + str(i)

    r = requests.get(URL_TEMPLATE)

    r.encoding = r.apparent_encoding

    soup = bs(r.text, "html.parser")

    title = soup.find_all('h1', itemprop = 'headline')

    print(title[0].string)

    text = soup.find('article', itemprop = 'articleBody').find_all('p')
    text_result = ''
    for t in text:
        text_result = text_result + str(t)
        print(t)

    cur.executemany("INSERT INTO _NewsSite_posts(Title, UserID_id, Datee, CategoryID_id, Text) VALUES(?, ?, ?, ?, ?)", [(title[0].string, 3, '2023-03-25 04:57:21.129307', random.randint(1, 10), text_result)])
    con.commit()

    time.sleep(5)


input()
