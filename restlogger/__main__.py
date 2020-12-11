import sys, getopt
import requests, logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')

file_handler = logging.FileHandler('l_restlogger.csv')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class My_Logger_Class():
    def __init__(self, url):
        self.url = url

    def set_request(self):
        req_data = requests.get(self.url)

        return req_data.json()

    def set_content(self, req_data):
        city_name = req_data['name']
        

def main():
    args = sys.argv[1:]
    logger.debug('count of args :: {}'.format(len(args)))


    my_object = My_Logger_Class('http://api.openweathermap.org/data/2.5/weather?q=Zurich,CHZH&appid=3836093dde650898eb014e6f27304646')


    my_dict = my_object.set_request()
    my_object.set_content(my_dict)


if __name__ == '__main__':
    main()

