import requests
import json
import random
from bs4 import BeautifulSoup

file = open('./config_pics.json')
config = json.load(file)

session = requests.session()
img_href = []
headers = {
    'authority': 'www.yeezysupply.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

def sites ():
    site = config['joyreactor']
    link = site[random.randint(0,len(site)-1)]
    print('rector use this link: ',link)
    return link

def lastes_page (site):
    response = session.get(site, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for element in soup.find_all('div', class_='pagination_expanded'):
        page = element.find('span', class_="current").text.strip()
        #print(type(page),page)
        page = random.randint(1, int(page))
    return page

def scan_content ():
    site = sites()
    link_to_page = site + '/' + str(lastes_page(site))
    #print('link to page', link_to_page)
    response_page = session.get(link_to_page, headers=headers)
    soup_page = BeautifulSoup(response_page.text, 'html.parser')
    for element in soup_page.find_all('div', class_='post_top'):
        posts_content = element.find('div', class_="image")
        if posts_content != None :
            img_href.append(posts_content.find('img').get('src'))
        #pic_link = pic_link.append(link_original_post.find('img'))
    url = img_href[random.randint(0,len(img_href)-1)]
    print('reactor url: ', url)
    return url

#print(scan_content())

