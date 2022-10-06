import pytest
from pprint import pformat
from pytest_api_suite.src.utils.misc.misc import *
from pytest_api_suite.src.utils.api.woocommerce_resources import WoocommerceApi
from pytest_api_suite.src.utils.dao.customers_dao import CustomersDAO

@pytest.mark.id29
@pytest.mark.smoke
def test_create_customer_only_email():
    logger.info('\nTEST: Create a new customer with email and password')

    cust_credentials = generate_random_email_pass()
    post_customer_body = {
        "email": cust_credentials['email']
    }
    create_customer_rs = WoocommerceApi().create_customer(post_customer_body)
    json_rs = create_customer_rs.json()
    assert create_customer_rs.status_code == 201

    logger.debug(f"Created user with email: {json_rs['email']}")
    assert cust_credentials['email'] == json_rs['email']
    # logger.debug(pformat(json_rs))

    db_rows = CustomersDAO().get_customer_by_email(cust_credentials['email'])
    assert len(db_rows) != 0, "SQL Query: Not Found, returned an empty list!!!"

    db_email = db_rows[0]['user_email']
    assert cust_credentials['email'] == db_email
    logger.debug(db_rows)

@pytest.mark.id30
def test_get_all_customers():
    logger.info('\nTEST: Get All Customers')
    get_customers_rs = WoocommerceApi().get_customers()
    assert get_customers_rs.status_code == 200

    json_rs = get_customers_rs.json()
    assert json_rs, f"Get All Customers: Empty JSON Response"
    logger.debug(f"Total Number of Customers: {len(json_rs)}")

@pytest.mark.id47
@pytest.mark.negative
def test_create_customer_existing_email():
    logger.info('\nTEST: Create Customer: existing-email')
    random_user = CustomersDAO().get_random_customers()
    existing_email = random_user[0]['user_email']
    logger.debug(existing_email)

    post_customer_body = {
        "email": existing_email
    }
    create_customer_rs = WoocommerceApi().create_customer(post_customer_body)
    json_rs = create_customer_rs.json()
    logger.debug(pformat(json_rs))

    expected_error_code = 'registration-error-email-exists'
    expected_error_msg = 'An account is already registered with your email address'
    assert create_customer_rs.status_code == 400
    assert json_rs['code'] == expected_error_code, f'Created customer with EXISTING USER {existing_email}' \
        f"Expected: '{expected_error_code}' \nActual: {json_rs['code']}"
    assert expected_error_msg in json_rs['message'], f"Expected: {expected_error_msg} \n" \
        f"Actual: {json_rs['message']}"






