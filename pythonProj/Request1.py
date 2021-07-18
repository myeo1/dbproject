# import urllib.request as urlb
# import pprint
#
# response_url = urlb.urlopen('https://api.publicapis.org/entries')
# print(response_url)
# print(response_url.info())
# print(response_url.read())
#
# html = response_url.read()
# pprint.pprint(html)
# response_url.close()

import requests

class GetRequests:
    def make_get_request(self, url):
        res = requests.get(url=url)

        if res.status_code == 200:
            print(res.headers)
        else:
            print(res.status_code)

urls = {'google': 'https://www.google.com'}
my_get = GetRequests()
my_get.make_get_request(urls['google'])
