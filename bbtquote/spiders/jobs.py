# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy import Request

from bbtquote.items import BbtquoteItem

from bbtquote.spiders import Character


class JobsSpider(Spider):
    name = 'jobs'
    allowed_domains = ['bigbangtrans.wordpress.com']
    start_urls = ['https://bigbangtrans.wordpress.com/']
    character = Character()

    def parse(self, response):
        jobs = response.xpath(
            '//ul/li[contains(@class, "page_item page-item-")]')
        for job in jobs:
            official_title = job.xpath('a/text()').extract_first()
            if official_title == 'About':
                continue
            relative_url = job.xpath('a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)
            season = official_title[7:9]
            episode = official_title[18:20]
            yield Request(absolute_url, callback=self.parse_page, meta={'Season': season, 'Episode': episode})

        item = BbtquoteItem()
        for name, quote in self.character._phrase.items():
            item['name'] = name
            item['quote'] = quote
            yield item

    def parse_page(self, response):
        season = response.meta.get('Season')
        episode = response.meta.get('Episode')

        content = self.extract_content(response, season, episode)
        self.character.append_phrase(content)

    def extract_content(self, response, season, episode):
        if (int(season) == 6 and int(episode)) == 1 or (int(season) == 7 and 1 <= int(episode) <= 15) or int(season) == 10:
            content = response.xpath(
                '//div[@class="entrytext"]/p/span/text()').extract()
        elif (int(season) >= 2 and int(episode) >= 2) or int(season) >= 3:
            content = response.xpath(
                '//div[@class="entrytext"]/p/text()').extract()
        else:
            content = response.xpath(
                '//div[@class="entrytext"]/p/span/text()').extract()
        return content
