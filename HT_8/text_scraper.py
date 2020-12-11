from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'

responce = requests.get(url)
if responce.ok:
    soup = BeautifulSoup(responce.text, 'lxml')
    quotes = soup.select('div[class = "quote"]')
    for quote in quotes:
        text = quote.select_one('span[class = "text"]').text
        author = quote.select_one('small[class = "author"]').text
        href = quote.select_one('a').get('href', '')
        if href:
            href = url + href[1:]
        # bio author
        responce_author = requests.get(href)
        if responce_author.ok:
            soup = BeautifulSoup(responce_author.text, 'lxml')
            bio = soup.select_one('div[class = "author-description"]').text
        print(f'text: {text}\nauthor: {author}\nurl: {href}\nbio: {bio}')
        print()



if __name__ == '__main__':
    pass