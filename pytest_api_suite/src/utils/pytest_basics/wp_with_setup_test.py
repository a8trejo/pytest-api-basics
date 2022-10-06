import pytest
from _pytest.junitxml import record_property

# This marks ALL tests on the file
pytestmark = [pytest.mark.api, pytest.mark.setUp]

@pytest.fixture(scope='module')
def my_setup():
    print("\n------------------PYTEST FIXTURE----------------------")
    return {'id': 20, 'name': 'Adams'}

@pytest.mark.happyPath
def test_login_valid_user(my_setup):
    print("Login with valid user")
    print(f"Name: {my_setup['name']}")

@pytest.mark.happyPath
def test_login_invalid_user(record_property):
    print("\nLogin with invalid user")
    record_property("example_key", 1)

@pytest.mark.negative
class TestCheckout(object):
    def test_checkout_as_guest(self):
        print("\nCheckout as guest!")