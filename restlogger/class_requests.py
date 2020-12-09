import requests
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')

file_handler = logging.FileHandler('log_requests.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Request_Class():
    def __init__(self, url_address):
        self.url_address = url_address

    def set_request(self):
        req_data = requests.get(self.url_address)

        r_dict = req_data.json()
        logger.debug('---------------------------')
        logger.debug(type(r_dict))
        logger.debug("---------------------------")

        return r_dict

    def parse_json(self, any_dict):
        logger.debug('--------test2--------')
        logger.debug(type(any_dict))
        


