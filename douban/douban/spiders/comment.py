import scrapy
from lxml import etree
import re


from douban.douban.items import CommentItem


class CommentSpider(scrapy.Spider):
    """
    豆瓣电影短评爬取
    """
    name = 'comment'

    movie_ids = ['34841067', '27619748', '26826330', '34880302', '34779692', '26935283', '34825886']

    def start_request(self):
        start_url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'
        for movie_id in self.movie_ids:
            for i in range(51):
                url = start_url.format(movie_id, str(i * 20))
                yield scrapy.Request(url=url, callback=self.parse, meta={'movie_id': movie_id})

    def parse(self, response):
        selector = etree.HTML(response.text)
        item = CommentItem()
        item['movie_id'] = response.meta['movie_id']
        item['user_name'] = selector.xpath('//span[@class="comment-info"]/a/text()')
        rating_star = selector.xpath('//span[@class="comment-info"]/span[2]/@class')
        if 'ranting' in rating_star:
            pattern = re.compile('\d+(\\.\\d+){0,1}')
            ranting = pattern.search(rating_star).group()
            item['rating'] = int(ranting)/10
        else:
            item['rating'] = None
        item['comment_time'] = selector.xpath('//span[@class="comment-time "]/@title')
        item['comment_info'] = selector.xpath('//p[@class=" comment-content"]/span/text()')
        item['votes_num'] = selector.xpath('//span[@class="votes vote-count"]/text()')
        item['user_url'] = selector.xpath('//span[@class="comment-info"]/a/@href')
        item['comment_date'] = selector.xpath('//span[@class="comment-time "]/text()')

        yield item
