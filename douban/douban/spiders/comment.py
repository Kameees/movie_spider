import scrapy
import re


from douban.items import CommentItem


class CommentSpider(scrapy.Spider):
    """
    豆瓣电影短评爬取
    """
    name = 'comment'

    allowed_domains = ['movie.douban.com']

    custom_settings = {
        'ITEM_PIPELINES': {'douban.pipelines.CommentPipeline': 302},
    }

    movie_ids = [
        '34841067',
        '27619748',
        '26826330',
        '34880302',
        '34779692',
        '26935283',
        '34825886']
    start_url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'
    start_urls = []
    for movie_id in movie_ids:
        for i in range(0, 26):
            start_urls.append(start_url.format(movie_id, str(i * 20)))

    def parse(self, response):
        comment_url = response.url
        pattern = re.compile(r'\d+(\\.\\d+){0,1}')
        comments = response.xpath('//div[@class="comment"]')
        for comment in comments:
            item = CommentItem()
            item['movie_id'] = pattern.search(comment_url).group()
            item['user_name'] = comment.xpath(
                './/span[@class="comment-info"]/a/text()').extract_first()
            rating_star = comment.xpath(
                './/span[@class="comment-info"]/span[2]/@class').extract_first()
            if pattern.search(rating_star):
                ranting = pattern.search(rating_star).group()
                item['rating'] = float(ranting) / 10
            else:
                item['rating'] = None
            item['comment_time'] = comment.xpath(
                './/span[@class="comment-time "]/@title').extract_first()
            item['comment_info'] = comment.xpath(
                './p[@class=" comment-content"]/span/text()').extract_first()
            item['votes_num'] = comment.xpath(
                './/span[@class="votes vote-count"]/text()').extract_first()
            item['user_url'] = comment.xpath(
                './/span[@class="comment-info"]/a/@href').extract_first()
            comment_date = comment.xpath(
                './/span[@class="comment-time "]/text()').extract_first()
            item['comment_date'] = comment_date.replace('\n', '').strip()
            yield item
