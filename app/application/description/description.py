from flask import Blueprint, jsonify
import sys
import os
from ..model.competition_info import CompetitionInformationModel

app = Blueprint('description', __name__)

@app.route('/api/v1/get/description/<competition_id>', methods=['GET'])
def get_description(competition_id):
    competition_model = CompetitionInformationModel()
    competition_model.setup_test_data()
    descriptions = competition_model.fetch_competition_information_by_id(competition_id)
    response = jsonify({'message':descriptions['competition_description']})
    response.status_code = 200
    return response

@app.route('/api/v1/get/competition/competitions/', methods=['GET'])
def get_all_competition_information():
    competition_model = CompetitionInformationModel()
    competition_model.setup_test_data()
    competition_info = competition_model.fetch_all_competition_information()
    for i in range(len(competition_info)):
        competition_info[i]['id'] = str(competition_info[i]['_id'])
        del competition_info[i]['_id']
    return jsonify(competition_info)