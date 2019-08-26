import subprocess
from time import sleep
import DAO_youtube as utub

rows = utub.get_undownloaded_videos()
cmd = 'youtube-dl --audio-format mp3 --audio-quality 0 --output "{path_dl}%(title)s.%(ext)s" -x {uri}'

for row in rows:
    id = row[utub.idx_id]
    uri = row[utub.idx_uri]
    subprocess.call(cmd.format(path_dl=utub.path_unclassified, uri=uri), shell=True)
    utub.update_download_video(id)
    sleep(5)

utub.close()