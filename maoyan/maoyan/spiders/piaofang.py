import scrapy
import json

from maoyan.items import MaoyanItem


class PiaofangSpider(scrapy.Spider):
    name = 'piaofang'
    allowed_domains = ['piaofang.maoyan.com']
    start_urls = ['http://piaofang.maoyan.com/getBoxList?date=1&isSplit=true']

    def parse(self, response):
        data = json.loads(response.text)
        data_list = data['boxOffice']["data"]["list"]
        for main_data in data_list:
            item = MaoyanItem()
            item["movie_id"] = main_data['movieInfo']["movieId"]
            item["movie_name"] = main_data['movieInfo']["movieName"]
            item["sum_box_desc"] = main_data['sumBoxDesc']
            item["box_desc"] = main_data['boxDesc']
            item["box_rate"] = main_data['boxRate']
            item["show_count_rate"] = main_data['showCountRate']
            item["seat_count_rate"] = main_data['seatCountRate']
            yield item
