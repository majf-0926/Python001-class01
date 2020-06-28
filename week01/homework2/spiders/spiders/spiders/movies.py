import scrapy
from bs4 import BeautifulSoup
from spiders.items import SpidersItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3']


    def parse(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'movie-hover-info'}).get_text().strip()
        item['content'] = content
        yield item
