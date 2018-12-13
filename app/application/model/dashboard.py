from pymongo import MongoClient
import os
import sys


class DashBoardModel:
    def __init__(self):
        self.client = MongoClient(
            'mongo', 27017, username='root', password='password')
        self.db = self.client.mlcompetition
        self.collection = self.db.dashboard

    def register_result(self, competition_id, file_name, result):
        new_posts = {'competition_id': competition_id,
                     'file_name': file_name,
                     'result': result}
        self.collection.insert_one(new_posts)
        return

    def fetch_all_result(self):
        all_result = self.collection.find({}, {'_id': False})
        return all_result

    def check_duplication(self, competition_id, file_name):
        duplicated_data = self.collection.find_one({'competition_id': competition_id,
                                  'file_name': file_name})
        return duplicated_data is not None