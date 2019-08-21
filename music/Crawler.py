import traceback
from time import sleep
from datetime import datetime
import os
import subprocess
import sqlite3

from selenium import webdriver
from selenium.common import exceptions

# start set & init
date = int(datetime.now().strftime('%Y%m%d'))

db_path = 'liked_list.db'
table_liked_video = 'LikedVideo'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS {}(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
uri TEXT NOT NULL,
date INTEGER NOT NULL,
status TEXT DEFAULT 'checked');'''.format(table_liked_video))

driver = webdriver.Chrome('bin/chromedriver')
# end set & init


def unlike_video(uri):
    driver.get(uri)
    driver.implicitly_wait(3)
    buttons = driver.find_elements_by_id('text')
    for b in buttons:
        try:
            aria_label = b.get_attribute('aria-label')
            if aria_label is not None and 'dislike' in aria_label:
                b.click()
        except:
            print(traceback.format_exc())
    pass



if __name__ == '__main__':
    get_liked_list()
    # download_video()
    # unlike_video('https://www.youtube.com/watch?v=ontU9cOg354&list=LL4PpeNycVxmn_ChBmvlbYww&index=2&t=0s')

    show_db()
    conn.commit()
    conn.close()
    driver.close()
