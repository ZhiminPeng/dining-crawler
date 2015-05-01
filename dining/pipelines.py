# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class FilterItem(object):
    def process_item(self, item, spider):
        # list of my favoriate dishes
        favoriate_list = ['salmon', 'lamb', 'steak',
                          'fried egg', 'seafood',
                          'bbq pork ribs', 'chicken wings', 'fried chicken']
        menu = item['menu']
        item['favor'] = []
        for dish in menu:
            flag = 0
            for my_favor in favoriate_list:
                if my_favor in dish:
                    flag = 1
            if flag is 1:
                item['favor'].append(dish)
                print dish
        # print item['favor']
        return item
