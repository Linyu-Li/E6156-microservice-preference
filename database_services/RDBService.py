import logging
import pymysql
from typing import *

import middleware.context as context

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class RDBService:
    def __init__(self):
        pass

    @classmethod
    def _get_db_connection(cls):
        db_info = context.get_db_info()
        logger.info("RDBService._get_db_connection:")
        logger.info("\t HOST = " + db_info['host'])
        db_connection = pymysql.connect(
            **db_info,
            autocommit=True
        )
        return db_connection

    @classmethod
    def run_sql(cls,
                sql_statement: str,
                args: Union[Tuple, List, Dict] = None,
                fetch: bool = False):
        conn = RDBService._get_db_connection()
        try:
            cur = conn.cursor()
            logger.info("SQL Statement: " + cur.mogrify(sql_statement, None))
            res = cur.execute(sql_statement, args=args)
            if fetch:
                res = cur.fetchall()
        except Exception as e:
            conn.close()
            logger.error(e)
            raise e
        return res

    @classmethod
    def get_where_clause_args(cls, template: Dict) -> Tuple:
        if template:
            terms, args = [], []
            for k, v in template.items():
                terms.append(k + "=%s")
                args.append(v)
            clause = " where " + " AND ".join(terms)
            return clause, args
        return "", None

    @classmethod
    def find_by_template(cls,
                         db_schema: str,
                         table_name: str,
                         template: Dict,
                         field_list: List):
        wc, args = RDBService.get_where_clause_args(template)
        fields = ",".join(field_list) if field_list else "*"
        sql = "select {} from {}.{}{}".format(
            fields, db_schema, table_name, wc)
        return RDBService.run_sql(sql, args, fetch=True)

    @classmethod
    def update_by_template(cls,
                           db_schema: str,
                           table_name: str,
                           template: Dict,
                           field_update: Dict):
        wc, args = RDBService.get_where_clause_args(template)
        field_update = ",".join(
            "{} = {}".format(k, v) for k, v in field_update.items())
        sql = "update {}.{} set {}{}".format(
            db_schema, table_name, field_update, wc)
        return RDBService.run_sql(sql, args)

    @classmethod
    def delete_by_template(cls,
                           db_schema: str,
                           table_name: str,
                           template: Dict):
        wc, args = RDBService.get_where_clause_args(template)
        sql = "delete from {}.{}{}".format(db_schema, table_name, wc)
        return RDBService.run_sql(sql, args)

    @classmethod
    def create(cls,
               db_schema: str,
               table_name: str,
               create_data: dict):
        cols, vals, args = [], [], []
        for k, v in create_data.items():
            cols.append(k)
            vals.append('%s')
            args.append(v)
        cols_clause = "(" + ",".join(cols) + ")"
        vals_clause = "values (" + ",".join(vals) + ")"
        sql = "insert into {}.{}{} {}".format(
            db_schema, table_name, cols_clause, vals_clause)
        return RDBService.run_sql(sql, args)

    @classmethod
    def find_by_prefix(cls,
                       db_schema: str,
                       table_name: str,
                       column_name: str,
                       value_prefix: str,
                       field_list: List = None):
        fields = ",".join(field_list) if field_list else "*"
        sql = "select {} from {}.{} where {} like '{}%'".format(
            fields, db_schema, table_name, column_name, value_prefix)
        return RDBService.run_sql(sql, fetch=True)
