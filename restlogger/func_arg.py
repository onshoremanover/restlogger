import sys, getopt, io

def my_argument_function(argv):
    argu = {
            'freq' : 300,
            'url' : 'http://api.openweathermap.org/data/2.5/weather?q=Zurich,CHZH&appid=3836093dde650898eb014e6f27304646',
            'xpath' : '',
            'key' : 'name' 
            }
    try:
        opts, args = getopt.getopt(argv,"hf:u:x:k:",["freq=","url=","xpath=","key="])
    except getopt.GetoptError:
        print('-f <freq> -u <url> -x <xpath> -k <key>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -f <freq> -u <url> -x <xpath> -k <key>')
            sys.exit()
        elif opt in ("-f", "--freq"):
            argu['freq'] = arg
            print('Freq is: ',argu['freq'])

        elif opt in ("-u", "--url"):
            argu['url'] = arg
            print('URL is: ',argu['url'])

        elif opt in ("-x", "--xpath"):
            argu['xpath'] = arg
            print('XPath is: ',argu['xpath'])

        elif opt in ("-k", "--key"):
            argu['key'] = arg
            print('Key is: ',argu['key'])

    return argu
