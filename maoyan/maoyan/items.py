# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id = scrapy.Field()
    movie_name = scrapy.Field()
    sum_box_desc = scrapy.Field()
    box_rate = scrapy.Field()
    show_count_rate = scrapy.Field()
    seat_count_rate = scrapy.Field()