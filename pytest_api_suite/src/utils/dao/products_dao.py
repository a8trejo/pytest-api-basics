from pytest_api_suite.src.utils.dao.db_utilities import DBUtility
import random

class ProductsDAO(object):
    def __init__(self):
        self.db_run = DBUtility()

    def get_random_products(self, qty=1):
        sql_query = "SELECT * FROM wp_posts WHERE post_type='product' LIMIT 200"
        sql_rows = self.db_run.execute_sql(sql_query)
        rows_sample = random.sample(sql_rows, qty)
        return rows_sample
