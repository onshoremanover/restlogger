import sys
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    my_function('hello world')

    my_object = MyClass('Thomas')
    my_object.say_Name()

if __name__ == '__main__':
    main()
