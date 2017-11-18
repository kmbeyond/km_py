#import pymysql
#import mysqlite3


class ItemModel:

    def __init__(self, name, price):
        self.name=name
        self.price = price

    def json():
        return {"name": self.name, "price": self.price}
