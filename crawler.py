# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
import requests
import json
import re
from bs4 import BeautifulSoup
from news_classify_newsdao import NewsDAO

# Naver News Crawler using Mongo DB


class NaverNewsCrawler(object):

    def __init__(self, newsdao):
        self.newsdao = newsdao

    def crawl_news(self, link):

        res = requests.get(link)
        content = res.content
        soup = BeautifulSoup(content)

        try:
            title = soup.find('h3', attrs={"id": "articleTitle"}).get_text().strip()
            content = soup.find('div', attrs={"id": "articleBodyContents"}).get_text().strip()
            content_re = re.sub(r'//.+\n.+{}', '', content)
            content = content_re.strip()
            written_time = soup.find('span', attrs={"class": "t11"}).get_text()
            written_time = datetime.datetime.strptime(written_time, "%Y-%m-%d %H:%M")

            print link
            print str(title)
            print str(content)
            print written_time
            print '-' * 80

            self.newsdao.save_news(link, str(title), str(content), written_time)

        except Exception as e:
            print '2', e

    def get_news_link(self):

        news_topic_number = ['100', '101', '102', '103', '104', '105']

        for i in news_topic_number:
            url_start = 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1={}'.format(i)
            for j in range(1, 10):
                url_page = url_start + '#&date=2016-12-14 00:00:00&page={}'.format(str(j))
        #         print url_page
                res = requests.get(url_page)
                content = res.content
                soup = BeautifulSoup(content)
                # soup_1 = soup.find_all('div', attrs={"class":"section_headline headline_subordi"})
                soup_1 = soup.find_all('a', href=True)

                for k in soup_1:
                    if 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1={}'.format(i) in k['href']:
                        link = k['href']
                        # print link
                        self.crawl_news(link)
                        print 'ws'

newsdao = NewsDAO()
crawler = NaverNewsCrawler(newsdao)
crawler.get_news_link()
