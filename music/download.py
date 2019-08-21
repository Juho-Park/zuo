import os
import subprocess
from time import sleep
import DAO_youtube as utub

rows = utub.get_undownloaded_videos()

for row in rows:
    id = row[utub.idx_id]
    title = row[utub.idx_title]
    uri = row[utub.idx_uri]
    subprocess.call('youtube-dl --audio-format mp3 --audio-quality 0 --output "mp3/{}.mp3" -x {}'.format(title, uri),
                    shell=True)
    while not os.path.isfile('mp3/{}.mp3'.format(title)) or os.path.isfile('mp3/{}.webm'.format(title)):
        print('wait for {}'.format(title))
        sleep(3)
    utub.update_download_video(id)
    sleep(5)
