import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.olx.ua/d/uk/hobbi-otdyh-i-sport/sport-otdyh/velo/khmelnitskiy/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_subcategory%5D%5B0%5D=velosipedy'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'accept': '*/*'
}
HOST = 'https://olx.ua'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='css-19ucd76')

    # bike=[]
    for item in items:
        # print(item.find('div', class_='css-u2ayx9'),'\n')
        print(item.find('h6'))
        print(item.find('div', class_='css-3xiokn'),)
        print(item.find('a', class_='css-1bbgabe').get('href'),'\n')
        # bike.append({
        #     'title': item.find('div', class_='css-19ucd76')
        # })
    # print(bike)
    print(len(items))




def parse():
    html = get_html(URL)
    # print(html.status_code)
    if html.status_code == 200:
        get_content(html.text)

    else:
        print('ErRROR')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse()
