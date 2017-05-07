from config import BaseConfig
import gridfs


class Userdb:
    client = BaseConfig.MONGOD_DATABASE_URI
    # client = MongoClient('localhost:27017')
    db = BaseConfig.DB_NAME
    # db = 'users'

    def __init__(self, coll):
        # self.db = db
        self.coll = coll

    def conn(self):
        return self.client[self.db][self.coll]

    def create_user(self, user_details):
        return self.conn().insert_one(user_details).inserted_id

    def update_user(self, user_details, new_data):
        return self.conn().update(user_details, {'$set': new_data}, True)

    def find_one_update(self, user_info, update_info):
        # has to be in the form of json pairs
        return self.conn().find_one_and_update(user_info, {'$push': update_info})

    def find_one(self, user_info):
        # has to be in the form of json pairs
        return self.conn().find(user_info).count()

    def find_user_details(self, user_info, criteria=""):
        return self.conn().find_one(user_info, criteria)

    def find_user(self, user_info):
        return self.conn().find_one(user_info)

    def find_users(self, user_info, criteria=""):
        return self.conn().find(user_info, criteria)

    def insert_many(self, data):
        return self.conn().insert_many(data)

    def coll_exist(self):
        return self.conn().count()

    def clear_old(self):
        return self.conn().delete_many({"email_checked": False})


class Testdb:
    client = BaseConfig.MONGOD_DATABASE_URI
    # client = MongoClient('localhost:27017')
    db = BaseConfig.DATABASE
    # db = 'users'

    def __init__(self):
        # self.db = db
        self.conn = gridfs.GridFS(self.db)

    def put(self, data):
        return self.put(data)

    def exists(self, user_info):
        # has to be in the form of json pairs
        return self.exists(user_info)

    def get(self, data):
        return self.get(data)

    def find_one(self, data):
        return self.find_one(data)

    def find(self, data):
        return self.find(data)
