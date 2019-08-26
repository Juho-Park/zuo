import os
import re
import subprocess as sp
import shutil

import DAO_youtube as utub

path_unclassified = utub.path_unclassified
path_classified = utub.path_classified
path_result = utub.path_mp3

if not os.path.isdir(path_classified):
    os.mkdir(path_classified)
if not os.path.isdir(path_unclassified):
    os.mkdir(path_unclassified)

files = os.listdir(path_unclassified)

for f in files:
    file_origin = '{path}{file}'.format(path=path_unclassified, file=f)
    p = sp.Popen('bpm-tag -f -n "{target}"'.format(target=file_origin),
                 shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    err, out = p.communicate()
    out = out.decode('utf-8')
    result = re.search('\d{2,3}\.\d{2,3}', out)
    bpm = round(float(result.group()))
    bpm_f = '{bpm}_{file}'.format(bpm=bpm, file=f)
    file_result = '{path}{file}'.format(path=path_result, file=bpm_f)
    shutil.copyfile(file_origin, file_result)
    shutil.move(file_origin, path_classified)
    print('move {origin}\n\t\tto {result}'.format(origin=file_origin, result=file_result))
