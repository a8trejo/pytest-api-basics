from pytest_api_suite.src.utils.dao.db_utilities import DBUtility
import logging as logger
import random

class CustomersDAO(object):
    def __init__(self):
        self.db_run = DBUtility()

    def get_customer_by_email(self, email):
        sql_query = f"SELECT * FROM wp_users WHERE user_email = '{email}'"
        logger.info(sql_query)
        sql_rows = self.db_run.execute_sql(sql_query)
        return sql_rows

    def get_all_customers(self):
        sql_query = f"SELECT * FROM wp_users"
        logger.info(sql_query)
        sql_rows = self.db_run.execute_sql(sql_query)
        return sql_rows

    def get_random_customers(self, qty=1):
        table_size_sql = "SELECT COUNT(*) AS number_of_rows FROM wp_users"
        table_size = self.db_run.execute_sql(table_size_sql)
        logger.debug(f"Number of customers: {table_size[0]['number_of_rows']}")
        random_index = random.randint(1, table_size[0]['number_of_rows'])

        sql_query = f"SELECT * FROM wp_users WHERE ID BETWEEN {random_index} and {random_index + qty -1}"
        logger.debug(sql_query)
        sql_rows = self.db_run.execute_sql(sql_query)
        return sql_rows
