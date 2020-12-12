import sys, getopt, io
import requests, logging
import json, csv


class My_Logger_Class():

    def __init__(self, argu):
        print('init start')
        self.argu = argu
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

    def set_content(self, req_data):
        uberdict = self.argu['xpath']
        key = self.argu['key']

        if uberdict == '':
            requested_data = req_data[key]
        elif key == '':
            requested_data = req_data[uberdict]
        else:
            requested_data = req_data[uberdict][key]

        print(requested_data)
        print("set_content done")
        return requested_data


    def logging(self, requested_data):
        pass
