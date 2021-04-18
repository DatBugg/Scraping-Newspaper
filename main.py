from bs4 import BeautifulSoup
import requests
import time

def titles_infobae():

    url = 'https://www.infobae.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all('h2', 'cst_hl dkt_fs_22')

    for t in titles:
        print(t.getText())
        print('')

if __name__ == '__main__':
    while True:
        titles_infobae()
        print('wating 60 secons... ')
        time.sleep(60)