from typing import *

from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class UserProfileResource(BaseRDBApplicationResource):
    db_name = "user_pref"
    table_name = "user_profile"
    table_str = db_name + "." + table_name

    def __init__(self):
        super().__init__()

    @classmethod
    def get_profile(cls, **kwargs) -> List:
        return RDBService.find_by_template(cls.db_name, cls.table_name, kwargs, ['movie', 'hobby', 'book', 'music', 'sports', 'major'])

    @classmethod
    def insert_profile(cls, **kwargs):
        return RDBService.create(cls.db_name, cls.table_name, kwargs)

    @classmethod
    def update_profile(cls, **kwargs):
        profile_id = kwargs.pop('id')
        return RDBService.update_by_template(
            cls.db_name, cls.table_name, {'id': profile_id}, kwargs)

    @classmethod
    def delete_profile(cls, **kwargs):
        return RDBService.delete_by_template(cls.db_name, cls.table_name, kwargs)

    @classmethod
    def get_links(cls, resource_data: Dict):
        raise NotImplementedError("TODO")

    @classmethod
    def get_data_resource_info(cls) -> Tuple[str, str]:
        return cls.db_name, cls.table_name
