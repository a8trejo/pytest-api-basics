import pytest
import logging as logger
from pytest_api_suite.src.utils.api.woocommerce_resources import WoocommerceApi
from pytest_api_suite.src.utils.dao.products_dao import ProductsDAO

@pytest.mark.id24
@pytest.mark.happyPath
def test_list_all_products():
    logger.info('\nTEST: Get All products: happy-path')

    get_products_rs = WoocommerceApi().get_products()
    assert get_products_rs.status_code == 200

    json_rs = get_products_rs.json()
    assert json_rs, f"Get All Products: Empty JSON Response"
    logger.debug(f"Total Number of Products: {len(json_rs)}")

@pytest.mark.id25
def test_get_product_by_id():
    logger.info('\nTEST: Get Product by ID: happy-path')

    # Get product from DB
    random_product = ProductsDAO().get_random_products()
    random_product_id = random_product[0]['ID']
    random_product_name = random_product[0]['post_title']

    # Get product from API and compare
    get_product_rs = WoocommerceApi().get_product_by_id(random_product_id)
    assert get_product_rs.status_code == 200

    json_rs = get_product_rs.json()
    assert json_rs, f"Get Product by ID: Empty JSON Response"

    assert json_rs['name'] == random_product_name, f"Product by ID returned wrong product" \
        f"Expected:{random_product_name} Received: {json_rs['name']}"
