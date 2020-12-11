import re
import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import os

# url = r'https://www.olx.ua/obyavlenie/honda-crw-2-4-2013god-avtomat-IDIfkQe.html'

def getNumber(url):
    # session& headers create
    session = requests.Session()
    session.headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'referer' : f'{url}'
    }
    # reg. ex.
    token_reg = r"var phoneToken = '(.*?)';" 
    site_id_reg = r"'id':'(.*?)',"

    response = session.get(url)
    # print('status_code: ', response.status_code)
    token = re.findall(token_reg, response.text)[0]
    site_id = re.findall(site_id_reg, response.text)[0]
    # print(f'token: {token}, site_id: {site_id}')

    phone_number_url_pattern = f'https://www.olx.ua/ajax/misc/contact/phone/{site_id}/?pt={token}'

    pn_response = session.get(phone_number_url_pattern).text
    phone = json.loads(pn_response)['value']
    return(phone)
    # print(phone)
    
def getName(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    name = soup.find('div', class_  = 'offer-user__actions').find('a').get_text(strip = True)
    return(name)
    # print(name)


site_map = r'https://www.olx.ua/sitemap.xml'
response = requests.get(site_map).text
soup = BeautifulSoup(response, 'lxml')
link_one = soup.find('sitemap').find('loc').get_text(strip = True)

response = requests.get(link_one).text
soup = BeautifulSoup(response, 'lxml')
link_catg = soup.find('url').find('loc').get_text(strip = True)

# create data.csv
# users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
# with open(users_data, 'w', newline= '') as write_file:
#      writer = csv.writer(write_file, delimiter = ';')
#      writer.writerow(['Names','Numbers'])

def parse(URL):
    HEADERS = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'offer-wrapper')
    # users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
    # write_file = open(users_data, 'a',newline= '')
    for item in items:
        try:
            link = item.find('a', class_ = 'marginright5 link linkWithHash detailsLink').get('href')
            name = getName(link)
            number = getNumber(link)
            print(name)
            print(number)
            # write data in data.csv
            # writer = csv.writer(write_file, delimiter = ';')
            # writer.writerow([f'{name}',f'{number}'])
            # timer
            time.sleep(1)
        except:
            continue
    # write_file.close()


parse(link_catg)