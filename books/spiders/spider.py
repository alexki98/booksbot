# -*- coding: utf-8 -*-
import scrapy


import requests

response = requests.get(
    "http://httpbin.scrapinghub.com/get",
    proxies={
        "http": "http://3f3819933c294d23b1e179c8b4d984ea:@proxy.crawlera.com:8010/",
    },
)
print(response.text)
