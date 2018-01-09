#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/9'

from bs4 import BeautifulSoup
import requests
import lxml
import re


def fetch_app_info_from_store():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML,'
                      ' like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    r = requests.get('http://www.qiushibaike.com', headers=headers)
    content = r.text
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    results = soup.find_all('div',
                            re.compile("article block untagged mb15 typs_*"))  # results = soup.select('content-left')
    for result in results:
        print result.find_all('div', 'content')[0].contents[1].text.replace('\n', '')
        # joke_text = result.span.get_text().replace(' ', '', 100)
        # print joke_text
        print '---------------------------'


if __name__ == '__main__':
    fetch_app_info_from_store()
