import scrapy
import re

class PostSpider(scrapy.Spider):
    name = "posts"

    start_urls = []
    
    list = []

    # page = str(input("Enter page: "))

    allowed_domains = ['https://stackoverflow.com/']
    
    for i in range(1,6):
        start_urls.append(
            "https://stackoverflow.com/questions/tagged/python?tab=newest&page=" +
            str(i) + "&pagesize=50")
   

    def parse(self, response):

        def formatString(str):
            str = re.sub("\n", " ", str)
            str = str.strip()
            str = re.sub(r"(?m)^[^\S\r\n]+", "", str)
            return str

        for post in response.css('div.s-post-summary'):
            content = post.css(
                'div.s-post-summary--content > .s-post-summary--content-excerpt::text'
            )[0].get()

            title = post.css(
                '.s-post-summary--content-title > .s-link::text')[0].get()

            yield {
                'No':
                post.css('div.s-post-summary::attr(data-post-id)')[0].get(),
                'Title':
                title,
                'Content':
                formatString(content),
                'Vote':
                post.css(
                    'div.js-post-summary-stats > div:nth-child(1) > span.s-post-summary--stats-item-number::text'
                )[0].get(),
                'Answer':
                post.css(
                    'div.js-post-summary-stats > div:nth-child(2) > span.s-post-summary--stats-item-number::text'
                )[0].get(),
                'View':
                post.css(
                    'div.js-post-summary-stats > div:nth-child(3) > span.s-post-summary--stats-item-number::text'
                )[0].get(),
                'Author':
                post.css(
                    '.s-user-card--info > .s-user-card--link > .flex--item::text'
                )[0].get()
            }
