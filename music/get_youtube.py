import traceback
from time import sleep

from selenium import webdriver
from selenium.common import exceptions

import DAO_youtube as utub

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('bin/chromedriver', chrome_options=options)
driver.get('https://www.youtube.com/playlist?list=LL4PpeNycVxmn_ChBmvlbYww')
for n in range(1, 50):
    driver.execute_script('window.scrollTo(0, {});'.format(1080 * n))
    sleep(0.1)

contents = driver.find_elements_by_id('content')

disable_video = ['Deleted video', 'Privated video', '삭제된 동영상', '비공개 동영상']

for c in contents:
    try:
        if c.text == '':
            print('passed no <a>')
            continue
        tag_a = c.find_element_by_tag_name('a')
        uri = tag_a.get_attribute('href')
        if 'watch' not in uri:
            print('passed {}'.format(uri))
            continue
        uri = uri.split('&list')[0]
        title = tag_a.find_element_by_id('meta').find_element_by_tag_name('h3').text
        if any(disable in title for disable in disable_video):
            print('skip disable video')
            continue
        is_exist = utub.get_id_by_uri(uri)
        if is_exist is not None:
            print('exist {}, then quit'.format(title))
            break
        utub.add_video(title, uri)
    except exceptions.NoSuchElementException:
        print(c.text)
        print('No such element exception occurred: {}'.format(traceback.format_exc()))
    except:
        print(c.text)
        print('Not expected exception occurred: {}'.format(traceback.format_exc()))
    finally:
        pass

driver.close()
utub.close()