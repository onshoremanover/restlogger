import sys, getopt, io
import requests, logging
import json, csv
from .func_arg import my_argument_function
from .class_logger import My_Logger_Class

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')

file_handler = logging.FileHandler('log_restlogger.csv')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
    print("main started")
    args = sys.argv[1:]
    logger.debug('count of args :: {}'.format(len(args)))
    print('count of args :: {}'.format(len(args)))

    for arg in args:
        print('passsed argument :: {}'.format(arg))

    argu = my_argument_function(sys.argv[1:]) 

    my_object = My_Logger_Class(argu)


    my_dict = my_object.set_request()
    city_name = my_object.set_content(my_dict)
    logger.debug(city_name)

    #help(My_Logger_Class)
    print("main done")

if __name__ == '__main__':
    main()

