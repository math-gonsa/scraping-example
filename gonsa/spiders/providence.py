# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader

from gonsa.items import Mapping
import scrapy


class Spider(scrapy.Spider):
    name = "providence"

    start_urls = ["http://www.imoveisprovidence.com.br/imoveis"]

    def parse(self, response):
        dominio = "https://" + response.url.split("/")[2]

        items = response.xpath(
            '//div[@class="listing-results"]/div[@class="col-sm-12 box-list"]'
        )

        for item in items:
            url = dominio + item.xpath("./div/a/@href").extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)

        next_page = response.xpath(
            '//a[@class="btn btn-md btn-primary btn-next"]/@href'
        ).extract_first()
        if next_page:
            next_page = dominio + next_page
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_detail(self, response):
        loader = ItemLoader(Mapping(), response=response)
        loader.add_value("url", response.url)
        loader.add_xpath("title", "normalize-space(//title/text())")
        yield loader.load_item()
