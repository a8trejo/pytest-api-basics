import pytest

# This marks ALL tests on the file
pytestmark = [pytest.mark.api, pytest.mark.functional]

@pytest.mark.happyPath
@pytest.mark.basics
def test_login_valid_user():
    print("\nLogin with valid user")

@pytest.mark.smoke
@pytest.mark.basics
def test_login_wrong_password():
    print("\nLogin with wrong password")

@pytest.mark.basics
def test_login_invalid_user():
    print("\nLogin with invalid user")

@pytest.mark.basics
class TestCheckout(object):
    def test_checkout_as_guest(self):
        print("\nCheckout as guest!")