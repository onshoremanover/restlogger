import sys, getopt, io
import requests, logging
import json, csv


class My_Logger_Class():

    def __init__(self, url):
        self.url = url
        print("init done")

    def __str__(self):
        pass

    def __eq__(self):
        pass


    def set_request(self):
        """The set_request function pulls the data from the API with the requests module and saves it as a python doct in req_data"""
        req_data = requests.get(self.url)
        print("set_request done")
        return req_data.json()

    def set_content(self, req_data):
        city_name = req_data['cod']
        print(city_name)
        print("set_content done")

