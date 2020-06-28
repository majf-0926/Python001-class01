# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        moviename = item['moviename']
        movietype = item['movietype']
        movietime = item['movietime']
        output = f'|{moviename}|\t|{movietype}|\t|{movietime}|\n\n'
        with open('./movies.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item