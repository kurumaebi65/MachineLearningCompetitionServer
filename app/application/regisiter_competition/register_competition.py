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
ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/api/v1/action/register_competition/", methods=['POST'])
def regisiter_competition():
    if request.method == 'POST':
        print(request, file=sys.stderr)
        if 'test_file' not in request.files or 'training_file' not in request.files:
            abort(400, {'error_message': 'No file part in request'})
        if 'competition_name' not in request.form or 'competition_description' not in request.form:
            abort(400, {'error_message': 'Invalid post'})
        return 'upload csv file'


@app.errorhandler(400)
def error_handler(error):
    response = jsonify({'message': error.description['error_message'],
                        'result': error.code})
    return response, error.code