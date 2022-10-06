import logging as logger
import random
import string


def generate_random_email_pass(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    e_domain = domain if domain is not None else 'coolsite.com'
    e_prefix = email_prefix if email_prefix is not None else 'testuser'

    random_email_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))
    random_email = f'{e_prefix}_{random_string}@{e_domain}'
    random_pass_length = 20
    random_pass = ''.join(random.choices(string.ascii_lowercase, k=random_pass_length))

    random_info = {'email': random_email, 'password': random_pass}
    logger.debug(f'Randomly generated mail and password: \n{random_info}')
    return random_info
