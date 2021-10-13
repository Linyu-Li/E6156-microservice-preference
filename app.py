from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging
# from datetime import datetime

# import utils.rest_utils as rest_utils

from application_services.pref_resource import UserProfileResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/profile', methods=['POST'])
def new_user_profile():
    # args passed via raw json in body
    profile = request.get_json().get('profile', {})
    if profile:
        res = UserProfileResource.insert_profile(**profile)
    else:
        res = -1
    return Response(json.dumps(res, default=str), status=200, content_type="application/json")


@app.route('/profile/<profile_id>', methods=['GET', 'PUT', 'DELETE'])
def user_profile(profile_id):
    """
    Reads, edits or deletes user profile records.

    Args:
        profile_id (int): ID of the user profile.

    Returns:
        response (Response): HTTP response

    """
    if request.method == 'GET':
        res = UserProfileResource.get_profile(id=profile_id)
    elif request.method == 'PUT':
        # args passed via raw json in body
        profile = request.get_json().get('profile', {})
        if profile:
            res = UserProfileResource.update_profile(id=profile_id, **profile)
        else:
            res = 0
    elif request.method == 'DELETE':
        res = UserProfileResource.delete_profile(id=profile_id)
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
