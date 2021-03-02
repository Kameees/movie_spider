# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class MovieInfoPipeline(object):
    def open_spider(self, spider):
        self.file = open('movie_info.csv', 'w', newline='', encoding='utf-8-sig')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['movie_id', 'movie_name', 'movie_year', 'movie_info', 'rating_num', 'rating', 'rating_sum', 'rating_info'])

    def process_item(self, item, spider):
        self.writer.writerow([item['movie_id'], item['movie_name'], item['movie_year'], item['movie_info'], item['rating_num'], item['rating'], item['rating_sum'], item['rating_info']])
        return item

    def close_spider(self, spider):
        self.file.close()


class CommentPipeline(object):

    def open_spider(self, spider):
        self.file = open('comment.csv', 'w', newline='', encoding='utf-8-sig')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['movie_id', 'user_name', 'rating', 'comment_time', 'comment_info', 'votes_num', 'user_url', 'comment_date'])

    def process_item(self, item, spider):
        self.writer.writerow([item['movie_id'], item['user_name'], item['rating'], item['comment_time'], item['comment_info'], item['votes_num'], item['user_url'], item['comment_date']])
        return item

    def close_spider(self, spider):
        self.file.close()
