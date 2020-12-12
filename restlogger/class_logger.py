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
        print(req_data)
        city_name = req_data[1]['title']
        print(city_name)
        print("set_content done")

