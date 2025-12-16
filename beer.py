import requests
from bs4 import BeautifulSoup

class Beer:
    """
    Represents a single beer.
    """
    def __init__(self, soup: BeautifulSoup) -> None:
        #grab id from href tag
        id_tag = soup.find('a', class_='label')
        self.id = int(id_tag['href'].split("/")[-1])

        #grab name/url
        name = soup.find('p', class_='name')
        self.name = name.text
        self.url = f"https://untappd.com{name.a['href']}"

        #grab img url
        self.img_url = soup.find('img')['src']      

        #grab brewery
        brewery_href = soup.find('p', class_='brewery').a['href']
        brewery_url = f"https://untappd.com{brewery_href}"
        brewery_soup = Brewery.find_brewery(brewery_url)
        self.brewery = Brewery(brewery_soup)

        #grab other details
        self.style = soup.find('p', class_='style').text
        self.abv = float(soup.find('p', class_='abv').text.strip().split("%")[0])
        self.ibu = int(soup.find('p', class_='ibu').text.strip().split()[0])
        self.rating = float(soup.find('div', class_='caps')['data-rating'])

    """
    Finds beer given search term by first opening the right serach page, then picking the first
    option.

    Params: search - search term to look up

    Returns: First result of search term's Untappd page html
    """
    @classmethod
    def find_beer(cls, search: str):
        search = search.replace(" ","+")
        #use User-Agent headers to get actual response
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        URL=f"https://untappd.com/search?q={search}&type=beer&sort=all"
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        #grab just the HTML of the first result
        return soup.find('div', class_='results-container').find('div', class_='beer-item')

class Brewery:
    """
    Represents a brewery
    """
    def __init__(self, soup: BeautifulSoup) -> None:
        self.name = soup.find('div', class_='name').h1.text.strip()

        loc = soup.find('p', class_='brewery').text.strip().split(",")
        self.city = loc[0]
        self.state = loc[1].split()[0]

        self.style = soup.find('p', class_='style').text

        ratings_str = soup.find('p', class_='raters').text.strip().split()[0]
        self.ratings = int(ratings_str.replace(",",""))

        self.site = soup.find('a', class_='url tip')['href']


    @classmethod
    def find_brewery(cls, url):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('div', class_='content')