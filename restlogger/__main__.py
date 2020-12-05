import sys
from .classmodule import My_Class
from .funcmodule import my_function
from .class_requests import Request_Class

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    my_function('hello world')

    my_object = My_Class('Lukas')
    my_object.say_name()

    my_object2 = Request_Class('http://api.openweathermap.org/data/2.5/weather?q=Zurich,CHZH&appid=3836093dde650898eb014e6f27304646')
    my_object2.request_an_url()


if __name__ == '__main__':
    main()
