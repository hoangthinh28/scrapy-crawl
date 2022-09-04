from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawldata.spiders.posts_spider import PostSpider
from scrapy import signals
from scrapy.signalmanager import dispatcher
import csv

def spider_results():
    results = []
    
    def crawler_results(signal, sender, item, response, spider):
        results.append(item)
        
    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    process = CrawlerProcess(get_project_settings())
    process.crawl(PostSpider)
    process.start()
    
    # with open('data.csv', 'w') as csvfile:
    #     fieldnames = ['Note', 'Title', 'Content', 'Vote', 'Answer', 'View']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for i in results:
    #         writer.writerow({'Note': i['No'], 'Title': i['Title'], 'Content': i['Content'], 'Vote': i['Vote'], 'Answer': i['Answer'], 'View': i['View'],})

if __name__ == '__main__':
    # print("ARRAY: " + str(spider_results()))
    spider_results()
    print("Export success!")