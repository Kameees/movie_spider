# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class MaoyanPipeline:
    def open_spider(self, spider):
        self.file = open('maoyan.csv', 'w', newline='', encoding='utf-8-sig')
        self.writer = csv.writer(self.file)
        self.writer.writerow(
            ['movie_id', 'movie_name', 'sum_box_desc', 'box_rate', 'show_count_rate', 'seat_count_rate'])

    def process_item(self, item, spider):
        self.writer.writerow(
            [item['movie_id'], item['movie_name'], item['sum_box_desc'], item['box_rate'], item['show_count_rate'],
             item['seat_count_rate']])
        return item

    def close_spider(self, spider):
        self.file.close()
