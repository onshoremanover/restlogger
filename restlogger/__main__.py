import sys, getopt, io, re
import requests, logging, threading, time
from queue import Queue
import json, csv
from .func_arg import my_argument_function
from .class_logger import My_Logger_Class



def main():
    print("main started")
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    for arg in args:
        print('passed argument :: {}'.format(arg))

    argu = my_argument_function(sys.argv[1:]) 

    my_object = My_Logger_Class(argu)

    my_dict = my_object.set_request()
    my_information = my_object.set_content(my_dict)
   
    my_object.set_header()

    yes_change = re.search("y", argu['change'], flags = re.I)

    if yes_change:
        my_object.logging_changes(my_information)
    else:
        my_object.logging_fixed(my_information)


    #help(My_Logger_Class)
    print("main done")

if __name__ == '__main__':
    main()

