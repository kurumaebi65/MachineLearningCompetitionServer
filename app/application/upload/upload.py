from ..model.dashboard import DashBoardModel
from ..model.competition_info import CompetitionInformationModel
from pymongo import MongoClient
from sklearn import metrics
import pandas as pd
import io
import logging
from flask import Blueprint
from flask import request, abort, jsonify
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append('../../')

logging.basicConfig(level=logging.DEBUG)

app = Blueprint("upload", __name__)

UPLOAD_FOLDER = '/home/app/resources/upload_folder'
ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/v1/action/upload/<id>", methods=['POST'])
def upload(id):
    if request.method == 'POST':
        print(request, file=sys.stderr)
        if 'file' not in request.files:
            abort(400, {'error_message': 'No file part in request'})
        file = request.files['file']
        if file.filename == '':
            abort(400, {'error_message': 'No file in request'})
        if file and allowed_file(file.filename):
            register_result, message = register_prediction_result(id, file)
            if register_result:
                response = jsonify({'message': 'accuracy : {}'.format(message)})
                response.status_code = 200
            else:
                response = jsonify({'message': message})
                response.status_code = 200
            return response
        return 'upload csv file'


@app.errorhandler(400)
def error_handler(error):
    response = jsonify({'message': error.description['error_message'],
                        'result': error.code})
    return response, error.code

def get_correct_data_path(id):
    competition_info_model = CompetitionInformationModel()
    competition_info = competition_info_model.fetch_competition_information_by_id(id)
    return competition_info['test_data_path']


def register_prediction_result(competition_id, file):
    dashboard_model = DashBoardModel()
    if dashboard_model.check_duplication(competition_id, file.filename):
        return False, 'file name is duplicated'
    correct_data_path = get_correct_data_path(competition_id)
    text_stream = io.StringIO(file.stream.read().decode('utf-8'))
    accuracy = check_accuracy(text_stream, correct_data_path)
    dashboard_model.register_result(competition_id,file.filename ,accuracy)
    return True, accuracy


def check_accuracy(file1, file2):
    file1_dataframe = pd.read_csv(file1)
    file1_column = file1_dataframe.loc[:, 'label']
    file2_dataframe = pd.read_csv(file2)
    file2_column = file2_dataframe.loc[:, 'label']
    accuracy = metrics.accuracy_score(file1_column, file2_column)
    return accuracy
