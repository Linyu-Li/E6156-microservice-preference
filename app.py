from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging
from datetime import datetime

import utils.rest_utils as rest_utils

from application_services.UsersResource.user_service import UserResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['GET', 'POST'])
def user_collection():
    """
    1. HTTP GET return all users.
    2. HTTP POST with body --> create a user, i.e --> database.
    :return:
    """
    res = UserResource.get_by_template(None)
    return Response(json.dumps(res, default=str), status=200, content_type="application/json")


@app.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def specific_user(user_id):
    """
    1. Get a specific one by ID.
    2. Update body and update.
    3. Delete would ID and delete it.
    :param user_id:
    :return:
    """
    pass


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
