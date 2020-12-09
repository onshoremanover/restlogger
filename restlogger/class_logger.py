import logging
import csv
import io

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')

file_handler = logging.FileHandler('l_restlogger.csv')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Logger_Class():
    def __init__(self, any_dict):
        self.any_dict = any_dict

    def set_content(self):
        city_name = self.any_dict['name']
        logger.info('name of city: {}'.format(city_name))

