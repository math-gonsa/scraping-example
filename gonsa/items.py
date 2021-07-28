from itemloaders.processors import TakeFirst
import scrapy


class Mapping(scrapy.Item):

    url = scrapy.Field(
        output_processor=TakeFirst(),
    )

    title = scrapy.Field(
        output_processor=TakeFirst(),
    )
