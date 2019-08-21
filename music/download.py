import DAO_youtube as utub

rows = utub.get_videos()

cursor.execute('SELECT MAX(date) FROM {}'.format(table_liked_video))
last_date = cursor.fetchone()[0]
cursor.execute("SELECT id, title, uri FROM {} WHERE date >= {} and status='checked'"
               .format(table_liked_video, last_date))
for row in cursor.fetchall():
    id = row[0]
    title = row[1]
    uri = row[2]
    subprocess.call('youtube-dl --audio-format mp3 --audio-quality 0 --output "mp3/{}.mp3" -x {}'.format(title, uri),
                    shell=True)
    while not os.path.isfile('mp3/{}.mp3'.format(title)) or os.path.isfile('mp3/{}.webm'.format(title)):
        print('wait for {}'.format(title))
        sleep(3)
    cursor.execute("UPDATE {} SET status='downloaded' WHERE id={}".format(table_liked_video, id))
    sleep(5)