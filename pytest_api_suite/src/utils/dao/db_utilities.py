import pymysql
import os
from pytest_api_suite.src.utils.misc.credentials_utilities import CredentialsUtility
from pytest_api_suite.src.configs.config import DB_CONFIG

class DBUtility:
    def __init__(self):
        self.db_keys = CredentialsUtility().get_db_credentials()
        self.env_key = os.environ.get('envKey', 'local')

    def wp_db_connect(self):
        db_host = DB_CONFIG['WORDPRESS_DB']['base_url'][self.env_key]
        db_port = DB_CONFIG['WORDPRESS_DB']['port'][self.env_key]
        db_name = DB_CONFIG['WORDPRESS_DB']['db_name']
        db_user = self.db_keys['db_user']
        db_pass = self.db_keys['db_password']
        db_connection = pymysql.connect(host=db_host, database= db_name,user=db_user, password=db_pass, port=db_port)

        return db_connection

    def execute_sql(self, sql_query):
        db_conn = self.wp_db_connect()
        try:
            cursor = db_conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql_query)
            sql_rows = cursor.fetchall()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql_query} \nError: {str(e)}")
        finally:
            db_conn.close()

        return sql_rows
