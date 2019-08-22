import DAO_youtube as utub

rows = utub.get_videos()
cnt_download = 0
for row in rows:
    print(row)
    if utub.stat_downloaded == row[utub.idx_status]:
        cnt_download += 1
print('total: {}, downloaded: {}'.format(len(rows), cnt_download))

utub.close()
