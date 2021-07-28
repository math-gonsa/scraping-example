from itemloaders.processors import TakeFirst
import scrapy


class Mapping(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    model = scrapy.Field(output_processor=TakeFirst())
    brand = scrapy.Field(output_processor=TakeFirst())
    type_vehicle = scrapy.Field(output_processor=TakeFirst())
    year_manufacture = scrapy.Field(output_processor=TakeFirst())
    milage = scrapy.Field(output_processor=TakeFirst())
    type_fuel = scrapy.Field(output_processor=TakeFirst())
    type_shift = scrapy.Field(output_processor=TakeFirst())
    type_steering = scrapy.Field(output_processor=TakeFirst())
    color = scrapy.Field(output_processor=TakeFirst())
    motor_power = scrapy.Field(output_processor=TakeFirst())
    number_of_doors = scrapy.Field(output_processor=TakeFirst())
    neighborhood = scrapy.Field(output_processor=TakeFirst())
    city = scrapy.Field(output_processor=TakeFirst())
