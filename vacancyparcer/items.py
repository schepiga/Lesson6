# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VacancyparcerItem(scrapy.Item):
    name = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    salary_curr = scrapy.Field()
    url = scrapy.Field()
    cite = scrapy.Field()
    _id = scrapy.Field()
