import scrapy
from lxml import etree
import re

from douban.douban.items import MovieItem


class MovieInfoSpider(scrapy.Spider):
    """
    豆瓣电影信息爬取
    电影ID：
    你好，李焕英：34841067
    唐人街探案3：27619748
    刺杀小说家：26826330
    人潮汹涌：34880302
    新神榜：哪吒重生：34779692
    侍神令：26935283
    熊出没·狂野大陆：34825886
    """
    name = 'movie_info'

    custom_settings = {
        'ITEM_PIPELINES': {'douban.pipelines.MovieInfoPipeline': 301},
    }

    movie_ids = ['34841067', '27619748', '26826330', '34880302', '34779692', '26935283', '34825886']

    def start_request(self):
        start_url = 'https://movie.douban.com/subject/{}/?from=showing'
        for movie_id in self.movie_ids:
            url = start_url.format(movie_id)
            yield scrapy.Request(url=url, callback=self.parse, meta={'movie_id': movie_id})

    def parse(self, response):
        selector = etree.HTML(response.text)
        item = MovieItem()
        item['movie_id'] = response.meta['movie_id']
        item['movie_name'] = selector.xpath('//span[@class="comment-info"]/a/text()')
        year = selector.xpath('//div[@id = "content"]/h1/span/text()')
        pattern = re.compile('(?<=\()[^}]*(?=\))')
        item['movie_year'] = pattern.search(year).group()
        item['movie_info'] = selector.xpath('//div[@id = "info"]//text()')
        item['rating_num'] = selector.xpath('//span[@class="comment-info"]/a/text()')
        rating_star = selector.xpath('//div[@class = "rating_right "]/div/@class')
        if 'ranting' in rating_star:
            pattern = re.compile('\d+(\\.\\d+){0,1}')
            ranting = pattern.search(rating_star).group()
            item['rating'] = int(ranting)/10
        else:
            item['rating'] = None
        item['rating_sum'] = selector.xpath('//div[@class = "rating_sum"]//span/text()')
        item['rating_info'] = selector.xpath('//div[@class = "ratings-on-weight"]//text()')

        yield item


