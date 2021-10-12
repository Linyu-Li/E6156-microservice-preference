from typing import *

from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class UserHobbyResource(BaseRDBApplicationResource):
    db_name = "user_pref"
    table_name = "user_hobby"
    table_str = db_name + "." + table_name

    def __init__(self):
        super().__init__()

    @classmethod
    def get_hobby(cls, **kwargs) -> List:
        return RDBService.find_by_template(cls.db_name, cls.table_name, kwargs, ['hobby'])

    @classmethod
    def insert_hobby(cls, **kwargs):
        return RDBService.create(cls.db_name, cls.table_name, kwargs)

    @classmethod
    def edit_hobby(cls, user_id: int, hobby_old: str, hobby_new: str):
        sql = "update {} set hobby = %s " \
              "where user_id = %s and hobby = %s".format(cls.table_str)
        return RDBService.run_sql(sql, (hobby_old, user_id, hobby_new))

    @classmethod
    def delete_hobby(cls, **kwargs):
        return RDBService.delete_by_template(cls.db_name, cls.table_name, kwargs)

    @classmethod
    def get_links(cls, resource_data: Dict):
        raise NotImplementedError("TODO")

    @classmethod
    def get_data_resource_info(cls) -> Tuple[str, str]:
        return cls.db_name, cls.table_name
