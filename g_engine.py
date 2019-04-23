import requests
from bs4 import BeautifulSoup

def search(film):
    url_endpoint = 'https://www.google.com/search'
    mydict = {'q': 'intitle index of {}'.format(film)}
    resp = requests.get(url_endpoint, params=mydict)
    return resp.text

def scrape(html_page):
    soup = BeautifulSoup(html_page,'lxml')
    results = soup.find_all('h3', {'class': 'r'})
    fetched = {}
    for result in results:
        raw = result.find('a').get('href')
        title = result.find('a').text
        i = raw.split('=')[1].split('&')[0]
        link = i.replace('25','')
        fetched[title]= link
    return fetched