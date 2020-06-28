import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3']

    def start_requests(self):
            yield scrapy.Request(
                self.start_urls[0], 
                callback=self.parse, 
                headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
                    #'Cookie':'_csrf=6e4e727f69ce37a6d0fb04f753dcfb3ea3644fa757da24d5c15e4dc8e7791735; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593347989; uuid_n_v=v1; mojo-uuid=3b9f197abe06a36bfff61f53b4fd8a10; uuid=2952DE70B82C11EA80F64D80EBA969F715F44B208D524338B04EE4F115DFE71D; _lxsdk_cuid=172f3f880c9c8-02dfa45b259f3a-71415a3a-17ed82-172f3f880c9c8; __mta=141934477.1593231049375.1593342751626.1593347989352.9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593231046,1593248063,1593342751; _lxsdk=2952DE70B82C11EA80F64D80EBA969F715F44B208D524338B04EE4F115DFE71D; _lxsdk_s=172faf0d8be-586-724-a6e%7C%7C3; mojo-trace-id=1; mojo-session-id={"id":"0b714d9698e46e1ed70b5db7ea709355","time":1593347989060}'
                })

    def parse(self, response): 
        item = SpidersItem()       
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div')       
        for movie in movies:
            item['moviename'] = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span[1]/text()')
            item['movietype'] = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[2]/text()')
            item['movietime'] = movie.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/text()')
            print('-----------')
            print(item['moviename'])
            print(item['movietype'])
            print(item['movietime'])
            print('-----------')
        yield item 
        
           