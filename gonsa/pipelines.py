from pymongo import MongoClient


class GonsaPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.database = self.client[self.mongo_db]

        self.database[spider.name].remove()

    def process_item(self, item, spider):

        item_processed = {k: v for k, v in item.items()}
        self.database[spider.name].insert_one(item_processed)
        return item

    def close_spider(self, spider):
        self.client.close()
        pass
