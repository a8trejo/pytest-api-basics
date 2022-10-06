# Virtual Env
python3 -m pip install virtualenv
which python3
python3 -m virtualenv --python=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 venv_py3
virtualenv --python=/Library/Frameworks/Python.framework/Versions/3.9/bin/python3 venv_py3
source venv_py3/bin/activate
deactivate
python setup.py install
python setup.py develop

# Pytest
# Test file names must start or end with 'test': 'test_*.py',  '*_test.py'

# Class names must start with 'Test' and methods with 'test_'

pytest <options>
pytest path/to/files
py.test path/to/files
python -m pytest <options>

pytest -v -s # With 'v' verbose to see the test functions, and 's' for printing stdout

# To run marked/tagged tests
pytest -m smoke
pytest -m "smoke or regression"
pytest -m "smoke and happyPath"
pytest -m "not prod"
pytest -v -s -m "setUp and not negative"
pytest -v -s -m "setUp and not negative" --log-cli-level=debug # Prints messages from logger
pytest --junitxml reports/testing-results.xml
pytest -v -s --junitxml reports/testing-results.xml
pytest -v -s -m "not basics" --junitxml reports/testing-results.xml

# To suppress mark warnings check pytest.ini

# To use @pytest.fixture(), the fixture function name needs to be passed as a parameter to the test function
# Similar to a before hook for a specific test
```
@pytest.fixture()
def my_setup():
    print("\n----------------------------------------")


@pytest.mark.happyPath
def test_login_valid_user(my_setup):
    print("\nLogin with valid user")
```
# You can specify @pytest.fixture(scope='module')

# For debugging
`import pdb; pdb.set_trace()`

# Extras
# https://dev.to/miyachin/there-are-many-options-for-connecting-mysql-from-python-but-lets-use-pymysql-or-mysql-connector-python-for-now-epe
# https://stackoverflow.com/questions/35579875/pytest-dynamically-generate-test-method
# https://docs.pytest.org/en/stable/how-to/parametrize.html