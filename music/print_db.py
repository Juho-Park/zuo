import DAO_youtube as utub

rows = utub.get_videos()
for row in rows:
    print(row)
print(len(rows))

utub.close()
