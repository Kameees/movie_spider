import scrapy
import re

from douban.items import MovieItem


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
    allowed_domains = ['movie.douban.com']

    custom_settings = {
        'ITEM_PIPELINES': {'douban.pipelines.MovieInfoPipeline': 301},
    }

    movie_ids = [
        '34841067',
        '27619748',
        '26826330',
        '34880302',
        '34779692',
        '26935283',
        '34825886']
    start_url = 'https://movie.douban.com/subject/{}/?from=showing'
    start_urls = []
    for movie_id in movie_ids:
        start_urls.append(start_url.format(movie_id))

    def parse(self, response):
        item = MovieItem()
        movie_url = response.url
        pattern = re.compile(r'\d+(\\.\\d+){0,1}')
        item['movie_id'] = pattern.search(movie_url).group()
        item['movie_name'] = response.xpath(
            '//div[@id = "content"]/h1/span/text()').extract_first()
        year = response.xpath(
            '//div[@id = "content"]/h1/span/text()').extract()[1]
        pattern = re.compile(r'(?<=\()[^}]*(?=\))')
        item['movie_year'] = pattern.search(year).group()
        movie_info = response.xpath('//div[@id = "info"]//text()').extract()
        item['movie_info'] = ''.join(movie_info).replace(
            ' ', '').replace(
            '\n', '')
        item['rating_num'] = response.xpath(
            '//strong[@class="ll rating_num"]/text()').extract_first()
        rating_star = response.xpath(
            '//div[@class = "rating_right "]/div/@class').extract_first()
        pattern = re.compile(r'\d+(\\.\\d+){0,1}')
        if pattern.search(rating_star):
            ranting = pattern.search(rating_star).group()
            item['rating'] = float(ranting) / 10
        else:
            item['rating'] = None
        item['rating_sum'] = response.xpath(
            '//div[@class = "rating_sum"]//span/text()').extract_first()
        rating_info = response.xpath(
            '//div[@class = "ratings-on-weight"]//text()').extract()
        item['rating_info'] = ''.join(rating_info).replace(
            ' ', '').replace(
            '\n', '')

        yield item
