# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    """
    movie_id：电影ID
    movie_name：电影名称
    sum_box_desc：总票房
    box_desc: 综合票房
    box_rate：综合票房占比
    show_count_rate：排片占比
    seat_count_rate：排坐占比
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id = scrapy.Field()
    movie_name = scrapy.Field()
    sum_box_desc = scrapy.Field()
    box_desc = scrapy.Field()
    box_rate = scrapy.Field()
    show_count_rate = scrapy.Field()
    seat_count_rate = scrapy.Field()