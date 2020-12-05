import requests

class Request_Class():
    def __init__(self, url_address):
        self.url_address = url_address
        
    def request_an_url(self):
        r = requests.get(self.url_address)

        print(r.text)

