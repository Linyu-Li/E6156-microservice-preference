from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging
# from datetime import datetime

# import utils.rest_utils as rest_utils

from application_services.pref_resource import UserHobbyResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/hobby/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_hobbies(user_id):
    """
    Reads, edits or deletes user hobby records.

    Args:
        user_id (int): ID of the user.

    Returns:
        response (Response): HTTP response

    """
    args_dict = request.get_json()  # args passed via raw json in body
    if request.method == 'GET':
        res = [ret['hobby'] for ret in UserHobbyResource.get_hobby(user_id=user_id)]
    elif request.method == 'POST':
        hobbies = args_dict.get('hobbies', [])
        res = sum([UserHobbyResource.insert_hobby(user_id=user_id, hobby=hobby)
                   for hobby in hobbies])
    elif request.method == 'PUT':
        hobby_old = args_dict.get('hobbyOld', None)
        hobby_new = args_dict.get('hobbyNew', None)
        if hobby_old and hobby_new:
            res = UserHobbyResource.edit_hobby(
                user_id=user_id, hobby_old=hobby_old, hobby_new=hobby_new)
        else:
            res = 0
    elif request.method == 'DELETE':
        hobbies = args_dict.get('hobbies', [])
        res = sum([UserHobbyResource.delete_hobby(user_id=user_id, hobby=hobby)
                   for hobby in hobbies])
    else:
        res = 0
    return Response(json.dumps(res, default=str), status=200, content_type="application/json")


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.find_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
