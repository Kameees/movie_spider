import scrapy
import re


from douban.items import CommentItem


class CommentSpider(scrapy.Spider):
    """
    豆瓣电影短评爬取
    """
    name = 'comment'

    allowed_domains = ['movie.douban.com']

    #   指定该spider运行的piplines为CommentPipeline
    custom_settings = {
        'ITEM_PIPELINES': {'douban.pipelines.CommentPipeline': 302},
    }

    #   将movie id及开始评论数填入url中组合获得需要爬取的url列表
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
            #   使用正则表达式匹配url中的movie_id
            item['movie_id'] = pattern.search(comment_url).group()
            item['user_name'] = comment.xpath(
                './/span[@class="comment-info"]/a/text()').extract_first()
            #   与movie_info相同，爬取豆瓣星级评分，因数据中没有直接的数字可获取，获取div中的class属性使用正则表达式取出数字进行处理获取星级评分
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
            #   清洗掉数据中的空格及换行符(\n)得到正确的日期
            comment_date = comment.xpath(
                './/span[@class="comment-time "]/text()').extract_first()
            item['comment_date'] = comment_date.replace('\n', '').strip()
            yield item
