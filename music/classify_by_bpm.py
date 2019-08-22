import os
import re
import subprocess as sp

import DAO_youtube as utub

path_work = utub.path_dl
path_result = utub.path_mp3

files = os.listdir(path_work)

for f in files:
    file_origin = '{path}{file}'.format(path=path_work, file=f)
    p = sp.Popen('bpm-tag -f -n "{target}"'.format(target=file_origin),
                 shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    err, out = p.communicate()
    out = out.decode('utf-8')
    result = re.search('\d{2,3}\.\d{2,3}', out)
    bpm = round(float(result.group()))
    bpm_f = '{bpm}_{file}'.format(bpm=bpm, file=f)
    file_result = '{path}{file}'.format(path=path_result, file=bpm_f)
    os.rename('{}'.format(file_origin),
              '{}'.format(file_result))
    print('move {origin}\n\t\tto {result}'.format(origin=file_origin, result=file_result))
