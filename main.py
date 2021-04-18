from bs4 import BeautifulSoup
import requests
import time

#Function that allows obtaining the titles under the H2 tag

def titles_infobae():

    url = 'https://www.infobae.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find_all('h2', 'cst_hl dkt_fs_22')

    for t in titles:
        print(t.getText())
        print('')


#I set the timer to get response every 5 mins

if __name__ == '__main__':
    while True:
        titles_infobae()
        print('wating 300 secons... ')
        time.sleep(60)