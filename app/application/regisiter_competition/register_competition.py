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

app = Blueprint("regisiter_competition", __name__)

UPLOAD_FOLDER = '/home/app/resources/upload_folder'
STATIC_FOLDER = '/home/app/static'
ALLOWED_EXTENSIONS = set(['csv'])
FILE_KIND = ['test_file', 'training_file', 'correct_file']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/v1/action/register_competition/", methods=['POST'])
def regisiter_competition():
    validation_request(request)
    training_file_name, test_file_name, correct_file_name = save_files(request)
    competition_name = request.form['competition_name']
    competition_description = request.form['competition_description']
    competition_info = CompetitionInformationModel()
    competition_info.register_competition_imformation(competition_name,
                                                      competition_description, 'classification', training_file_name, test_file_name, correct_file_name)
    return 'upload csv file'


@app.errorhandler(400)
def error_handler(error):
    response = jsonify({'message': error.description['error_message'],
                        'result': error.code})
    return response, error.code


def validation_request(request):
    # validation file in request
    if not all([x in request.files for x in FILE_KIND]):
        print([x in request.files for x in FILE_KIND], file=sys.stderr)
        abort(400, {'error_message': 'No file part in request'})
    test_file = request.files['test_file']
    training_file = request.files['training_file']
    correct_file = request.files['correct_file']
    if test_file.filename == '' or training_file.filename == '' or correct_file.filename == '':
        print('fuga', file=sys.stderr)
        abort(400, {'error_message': 'No file in request'})
    if not((test_file and allowed_file(test_file.filename)) and (training_file and allowed_file(training_file.filename)) and (correct_file and allowed_file(correct_file.filename))):
        print('hoge', file=sys.stderr)
        abort(400, {'error_message': 'No file in request'})

    # validation for form in request
    if 'competition_name' not in request.form or 'competition_description' not in request.form:
        abort(400, {'error_message': 'Invalid post'})


def save_files(request):
    test_file = request.files['test_file']
    training_file = request.files['training_file']
    correct_file = request.files['correct_file']
    test_file_name = secure_filename(test_file.filename)
    training_file_name = secure_filename(training_file.filename)
    correct_file_name = secure_filename(correct_file.filename)
    test_file.save(os.path.join(STATIC_FOLDER, test_file_name))
    training_file.save(os.path.join(STATIC_FOLDER, training_file_name))
    training_file.save(os.path.join(UPLOAD_FOLDER, correct_file_name))
    return training_file_name, test_file_name, correct_file_name
