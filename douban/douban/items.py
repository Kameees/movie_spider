# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    """
    movie_id：电影id（存于url中）
    movie_name：电影名称
    movie_year：上映年份
    movie_info：电影信息（导演、演员等信息）
    rating_num：豆瓣评分（分数，最高10分）
    rating：豆瓣星级评分（最高五星）
    rating_sum：参与评分总人数
    rating_info：豆瓣星级评分详情
    """
    movie_id = scrapy.Field()
    movie_name = scrapy.Field()
    movie_year = scrapy.Field()
    movie_info = scrapy.Field()
    rating_num = scrapy.Field()
    rating = scrapy.Field()
    rating_sum = scrapy.Field()
    rating_info = scrapy.Field()


class CommentItem(scrapy.Item):
    """
    movie_id：电影id（存于url中）
    user_name：用户名
    rating：用户评分
    comment_time：评论时间
    comment_info：评论内容
    votes_num：赞同人数
    user_url：用户url
    comment_date：评论日期
    """
    movie_id = scrapy.Field()
    user_name = scrapy.Field()
    rating = scrapy.Field()
    comment_time = scrapy.Field()
    comment_info = scrapy.Field()
    votes_num = scrapy.Field()
    user_url = scrapy.Field()
    comment_date = scrapy.Field()
