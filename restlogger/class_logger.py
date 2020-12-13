import sys, getopt, io
import requests, logging
import json, csv
from datetime import datetime

filename = 'log_test.csv'
delim = '|'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s"+delim+"%(levelname)s"+delim+"%(message)s")
file_handler = logging.FileHandler(filename)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class My_Logger_Class():

    def __init__(self, argu):
        print('init start')
        self.argu = argu
        self.key_name = argu['key'] 
        print(argu)
        print("init done")

    def __str__(self):
        pass

    def __eq__(self):
        pass


    def set_request(self):
        """The set_request function pulls data from the API with the requests module & saves python doct in req_data"""

        req_data = requests.get(self.argu['url'])
        print("set_request done")
        return req_data.json()

    def set_content(self, req_key):
        uberdict = self.argu['xpath']
        key = self.argu['key']

        if uberdict == '':
            requested_data = req_key[key]
        elif key == '':
            requested_data = req_key[uberdict]
            self.key_name = uberdict
        else:
            requested_data = req_key[uberdict][key]

        print(requested_data)
        print("set_content done")

        return requested_data

    def set_header(self):

        now = datetime.now()
        now = now.strftime("%H:%M:%S")

        f = open(filename, "a")
        f.write("Logging in file {} beginning at {}\n".format(filename, now))
        f.write("YYYY-MM-DD hh-mm-ss,mil Level {}\n".format(self.key_name))
        f.close()

    def logging_fixed(self, requested_data):
        logger.debug('test3 '+'executed fixed')

    def logging_changes(self, requested_data):
        logger.debug('test4 '+'executed changes')












