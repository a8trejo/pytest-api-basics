import json
import requests
import logging as logger

# To change the logging level of the 'requests' lib
# logging.getLogger("requests").setLevel(logging.WARNING)

class ApiUtilities(object):

    def post(self, endpoint, payload=None, auth=None, headers=None):
        if not headers:
            headers = {"Content-Type": "application/json"}

        rs_api = requests.post(url=endpoint, data=json.dumps(payload), headers=headers, auth=auth)
        # Log something similar to cy.api?
        logger.info(f"POST API response: {rs_api.status_code}")
        return rs_api

    def get(self, endpoint, auth=None, headers=None, qs=None, payload=None, path_params=None):

        get_rs = requests.get(url=endpoint, headers=headers, auth=auth, params=qs)
        logger.info(f"GET API response: {get_rs.status_code}")
        return get_rs
