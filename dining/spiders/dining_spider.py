# spider for crawling the dining hall website
import scrapy
from datetime import date
from dining.items import DiningItem
today = date.today()


class DiningSpider(scrapy.Spider):
    name = "dining"

    # check the url for the dining hall dinner menu
    start_urls = [
        # link for Covel
        'http://menu.ha.ucla.edu/foodpro/default.asp?location=07&date='
        + str(today.month) + "%2F" + str(today.day) +
        "%2F2015&meal=3&threshold=2",
        # link for De Neve
        'http://menu.ha.ucla.edu/foodpro/default.asp?location=01&date='
        + str(today.month) + "%2F" + str(today.day) +
        "%2F2015&meal=3&threshold=2",
        # link for Bruin Plate
        'http://menu.ha.ucla.edu/foodpro/default.asp?location=02&date='
        + str(today.month) + "%2F" + str(today.day) +
        "%2F2015&meal=3&threshold=2",
        # link for Feast
        'http://menu.ha.ucla.edu/foodpro/default.asp?location=04&date='
        + str(today.month) + "%2F" + str(today.day) +
        "%2F2015&meal=3&threshold=2"
    ]
    # parse function to parse the data and send an email to friends

    def parse(self, response):
        # list of entries in today's menu
        menu = response.xpath('//ul/li/a/text()').extract()
        temp = response.xpath('//span/a/text()').extract()
        hall_name = temp[1]
        menu = [item.lower() for item in menu]
        link = response.url
        item = DiningItem()
        item['menu'] = menu
        item['hall_name'] = hall_name
        item['link'] = link
        return item
