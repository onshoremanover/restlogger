import sys, getopt, io

def my_argument_function(argv):
    argu = {
            'freq' : 300,
            'url' : 'https://raw.githubusercontent.com/walter-rothlin/Source-Code/master/DatenFiles/JSON/todos_Small.json',
            'xpath' : 'title'
            }
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
            argu['freq'] = arg
            print('Freq is: ',argu['freq'])
        elif opt in ("-u", "--url"):
            argu['url'] = arg
            print('URL is: ',argu['url'])
        elif opt in ("-x", "--xpath"):
            argu['xpath'] = arg
            print('XPath is: ',argu['xpath'])

    return argu
