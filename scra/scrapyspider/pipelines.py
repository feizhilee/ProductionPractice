# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapyspider.dao.JobDao import JobDao

class ScrapyspiderPipeline:
    def process_item(self, item, spider):
        print(item['book_name'], item['book_introduction'], item['writer'], item['publisher'],
              item['price'], item['book_grade'], item['recommend_reason'], item['book_type'])
        jobDao = JobDao()
        try:
            params =[item['book_name'], item['book_introduction'], item['writer'], item['publisher'],
                     item['price'], item['book_grade'], item['recommend_reason'], item['book_type']]
            result = jobDao.createJobs(params)
            if result == 1:
                print("写入成功")
                pass
        finally:
            jobDao.close()
            pass


        return item
