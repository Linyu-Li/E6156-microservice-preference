from abc import ABC, abstractmethod
from database_services.RDBService import RDBService


class BaseApplicationException(Exception):

    def __init__(self):
        pass


class BaseApplicationResource(ABC):

    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def get_by_template(cls, template):
        pass

    @classmethod
    @abstractmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    @abstractmethod
    def get_data_resource_info(cls):
        pass


class BaseRDBApplicationResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_template(cls, template, field_list=None):
        db_name, table_name = cls.get_data_resource_info()
        res = RDBService.find_by_template(
            db_name, table_name, template, field_list)
        return res

    @classmethod
    @abstractmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    @abstractmethod
    def get_data_resource_info(cls):
        pass
