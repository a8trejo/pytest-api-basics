from setuptools import setup, find_packages

setup(name='pytest_api_suite',
      version='1.0',
      description="API testing with Pytest",
      author='Abel Trejo',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
        "black >= 22.1.0",
        "mysql-connector-python >= 8.0.30",
        "pytest >= 6.2.5",
        "requests >= 2.27.1",
        "requests-oauthlib >= 1.3.1",
        "PyMySQL >= 1.0.2",
        "requests_oauthlib"
      ]
      )
