import sys, getopt, io

def my_argument_function(argv):
    argu = {
            'freq' : 5,
            'url' : 'http://api.openweathermap.org/data/2.5/weather?q=Zurich,CHZH&appid=3836093dde650898eb014e6f27304646',
            'xpath' : '',
            'key' : 'name', 
            'change' : 'no',
            }
    try:
        opts, args = getopt.getopt(argv,"hf:u:x:k:c:",["freq=","url=","xpath=","key=","change="])
    except getopt.GetoptError:
        print('-f <freq> -u <url> -x <xpath> -k <key> -c <y/n>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -f <freq> -u <url> -x <xpath> -k <key> -c <y/n>')
            sys.exit()
        elif opt in ("-f", "--freq"):
            argu['freq'] = arg

        elif opt in ("-u", "--url"):
            argu['url'] = arg

        elif opt in ("-x", "--xpath"):
            argu['xpath'] = arg

        elif opt in ("-k", "--key"):
            argu['key'] = arg
        
        elif opt in ("-c", "--change"):
            argu['change'] = arg

    return argu
