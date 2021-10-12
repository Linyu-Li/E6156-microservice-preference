import os
from pymysql.cursors import DictCursor


def get_db_info():
    """
    Returns:
        A dictionary with connect info for MySQL Server.
    """
    db_host = os.environ.get("DBHOST", None)
    db_user = os.environ.get("DBUSER", None)
    db_password = os.environ.get("DBPASSWORD", None)

    if db_host is not None and db_user is not None and db_password is not None:
        db_info = {
            "host": db_host,
            "user": db_user,
            "password": db_password,
            "cursorclass": DictCursor
        }
    else:
        db_info = {
            "host": "fall2021.ccs6dqdhx73p.us-east-2.rds.amazonaws.com",
            "user": "admin",
            "password": "6156password",
            "cursorclass": DictCursor
        }

    return db_info
