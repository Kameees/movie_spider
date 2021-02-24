# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    movie_id = scrapy.Field()
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()
    movie_info = scrapy.Field()
    rating_num = scrapy.Field()
    rating = scrapy.Field()
    rating_sum = scrapy.Field()
    rating_info = scrapy.Field()


class CommentItem(scrapy.Item):
    movie_id = scrapy.Field()
    user_name = scrapy.Field()
    rating = scrapy.Field()
    comment_time = scrapy.Field()
    comment_info = scrapy.Field()
    votes_num = scrapy.Field()
    user_url = scrapy.Field()
    comment_date = scrapy.Field()
