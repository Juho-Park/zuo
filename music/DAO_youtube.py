from datetime import datetime

import sqlite3

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


def get_cursor():
    return cursor


def add_video(title, uri):
    cursor.execute('INSERT INTO LikedVideo (title, uri, date) VALUES (?, ?, ?);',
                   (title, uri, date))
    print('inserted {}'.format(title))


def get_videos():
    cursor.execute('SELECT * FROM {}'.format(table_liked_video))
    return cursor.fetchall()


def get_id_by_uri(uri):
    cursor.execute("SELECT id FROM {} WHERE uri='{}'".format(table_liked_video, uri))
    return cursor.fetchone()


def close():
    conn.commit()
    conn.close()
