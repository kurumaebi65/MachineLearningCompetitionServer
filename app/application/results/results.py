from flask import Blueprint, jsonify
import sys
import os
from ..model.dashboard import DashBoardModel

app = Blueprint('result', __name__)


@app.route('/api/v1/get/result/<competition_id>', methods=['GET'])
def get_result(competition_id):
    dashboard_model = DashBoardModel()
    results = dashboard_model.fetch_all_result()
    results_list = list(results)
    response = jsonify({'message':results_list})
    response.status_code = 200
    return response
