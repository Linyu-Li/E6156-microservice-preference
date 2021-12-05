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


@app.route('/api/profile', methods=['POST'])
def new_user_profile():
    # args passed via raw json in body
    profile = request.get_json()
    if profile and 'id' in profile:
        try:
            ret = UserProfileResource.insert_profile(**profile)
            if ret:
                res = 'Profile created!'
                status_code = 201
            else:
                res = 'Failed to create the profile!'
                status_code = 422
        except Exception as e:
            res = 'Database error: {}'.format(str(e))
            status_code = 422
    else:
        res = 'New profile cannot be empty or without an ID!'
        status_code = 400
    return Response(f"{status_code} - {res}", status=status_code, mimetype="application/json")


@app.route('/api/profile/<profile_id>', methods=['GET', 'PUT', 'DELETE'])
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
        if len(res):
            return Response(json.dumps(res[0], default=str), status=200, content_type="application/json")
        else:
            res = 'Resource not found!'
            status_code = 404
    elif request.method == 'PUT':
        # args passed via raw json in body
        profile = request.get_json()
        if len(profile):
            res = UserProfileResource.update_profile(id=profile_id, **profile)
            status_code = 200
        else:
            res = 'New profile cannot be empty!'
            status_code = 400
    else:  # elif request.method == 'DELETE':
        res = UserProfileResource.delete_profile(id=profile_id)
        status_code = 204
    return Response(f"{status_code} - {res}", status=status_code, mimetype="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
