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
status TEXT DEFAULT '{}');'''.format(table_liked_video, stat_check))

idx_id = 0
idx_title = 1
idx_uri = 2
idx_date = 3
idx_status = 4

stat_check = 'checked'
stat_downloaded = 'downloaded'


def get_cursor():
    return cursor


def add_video(title, uri):
    cursor.execute('INSERT INTO LikedVideo (title, uri, date) VALUES (?, ?, ?);',
                   (title, uri, date))
    print('inserted {}'.format(title))


def get_videos():
    cursor.execute('SELECT * FROM {}'.format(table_liked_video))
    return cursor.fetchall()


def get_undownloaded_videos():
    cursor.execute("SELECT * FROM {} WHERE status='checked' LIMIT 10".format(table_liked_video))
    return cursor.fetchall()


def get_id_by_uri(uri):
    cursor.execute("SELECT id FROM {} WHERE uri='{}'".format(table_liked_video, uri))
    return cursor.fetchone()


def update_download_video(id):
    cursor.execute("UPDATE {} SET status='{}' WHERE id='{}'".format(table_liked_video,stat_downloaded , id))
    print('update status id: {}'.format(id))


def close():
    conn.commit()
    conn.close()
