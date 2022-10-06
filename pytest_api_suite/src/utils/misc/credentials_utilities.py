import os

class CredentialsUtility(object):
    @staticmethod
    def get_wc_credentials():
        client_key = os.environ.get('WC_KEY')
        client_secret = os.environ.get('WC_SECRET')

        if not client_key or not client_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be in env variable")
        else:
            return {'client_key': client_key, 'client_secret': client_secret}

    @staticmethod
    def get_db_credentials():
        env_key = os.environ.get('envKey', 'local')
        db_user_key = f"DB_USER_{env_key.upper()}"
        db_pass_key = f"DB_PASSWORD_{env_key.upper()}"
        db_user = os.environ.get(db_user_key)
        db_password = os.environ.get(db_pass_key)

        if not db_user or not db_password:
            raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable")
        else:
            return {'db_user': db_user, 'db_password': db_password}
