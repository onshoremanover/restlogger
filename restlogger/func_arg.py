import sys, getopt, io

def my_argument_function(argv):
    freq = ''
    url = ''
    xpath = ''
    try:
        opts, args = getopt.getopt(argv,"hf:u:",["freq=","url=","xpath="])
    except getopt.GetoptError:
        print('-f <freq> -u <url> -x <xpath>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -f <freq> -u <url> -x <xpath>')
            sys.exit()
        elif opt in ("-f", "--freq"):
            freq = arg
            print('Freq is: ',freq)
        elif opt in ("-u", "--url"):
            url = arg
            print('URL is: ',url)
        elif opt in ("-x", "--xpath"):
            xpath = arg
            print('XPath is: ',xpath)

