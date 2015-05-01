#!/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd /Users/zhimin/Documents/coding/crawler/dining
scrapy crawl dining
python ./send_email.py
