import os
import logging as logger
from requests_oauthlib import OAuth1
from pytest_api_suite.src.configs.config import WOOCOMMERCE_API
from pytest_api_suite.src.utils.api.api_utilities import ApiUtilities
from pytest_api_suite.src.utils.misc.credentials_utilities import CredentialsUtility

logger.getLogger("requests_oauthlib").setLevel(logger.WARNING)
logger.getLogger("oauthlib").setLevel(logger.WARNING)
logger.getLogger("urllib3").setLevel(logger.WARNING)

class WoocommerceApi(object):

    def __init__(self):
        self.env = os.environ.get('envKey', 'local')
        self.base_url = WOOCOMMERCE_API['base_url'][self.env] + WOOCOMMERCE_API['api_path']['v3']

        api_keys = CredentialsUtility.get_wc_credentials()
        wc_client_key = api_keys['client_key']
        wc_client_secret = api_keys['client_secret']

        self.auth = OAuth1(wc_client_key, wc_client_secret)
        self.api = ApiUtilities()

    def create_customer(self, json_payload, **kwargs):
        create_customer_path = WOOCOMMERCE_API['endpoints']['customers']
        create_customer_endpoint = f'{self.base_url}{create_customer_path}'

        create_customer_rs = self.api.post(create_customer_endpoint, json_payload, self.auth)
        return create_customer_rs

    def get_customers(self):
        get_customers_path = WOOCOMMERCE_API['endpoints']['customers']
        get_customers_endpoint = f'{self.base_url}{get_customers_path}'

        get_customers_rs = self.api.get(get_customers_endpoint, self.auth)
        return get_customers_rs

    def get_products(self):
        get_products_path = WOOCOMMERCE_API['endpoints']['products']
        get_products_endpoint = f'{self.base_url}{get_products_path}'

        get_products_rs = self.api.get(get_products_endpoint, self.auth)
        return get_products_rs

    def get_product_by_id(self, product_id):
        get_product_path = WOOCOMMERCE_API['endpoints']['products']
        get_product_endpoint = f'{self.base_url}{get_product_path}/{product_id}'

        get_product_rs = self.api.get(get_product_endpoint, self.auth)
        return get_product_rs


