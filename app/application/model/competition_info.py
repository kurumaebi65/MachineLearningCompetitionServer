from pymongo import MongoClient
import os
import sys
from bson.objectid import ObjectId


class CompetitionInformationModel:
    def __init__(self):
        self.client = MongoClient(
            'mongo', 27017, username='root', password='password')
        self.db = self.client.mlcompetition
        self.collection = self.db.competition_information

    def register_competition_imformation(self, competition_name, competition_description, competition_type, training_data_path, test_data_path):
        new_post = {'competition_name': competition_name,
                    'competition_description': competition_description,
                    'competition_type' : competition_type,
                    'training_data_path': training_data_path,
                    'test_data_path': test_data_path}
        self.collection.insert_one(new_post)
        return

    def fetch_all_competition_information(self):
        all_result = self.collection.find({},{'competition_description':False,
        'training_data_path':False,'test_data_path':False})
        return list(all_result)

    def fetch_competition_information_by_id(self, competition_id):
        result = self.collection.find_one({'_id':ObjectId(competition_id)})
        return result

    def check_duplication(self, competition_name):
        duplicated_data = self.collection.find_one({'competition_name': competition_name})
        return duplicated_data is not None

    def setup_test_data(self):
        if not self.check_duplication('kyoto corpus challenge'):
            self.register_competition_imformation('kyoto corpus challenge',
            '# 京都コーパスチャレンジ','NLP, classificaiton','','resources/ans1.csv')