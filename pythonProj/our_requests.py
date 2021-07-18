import requests
# response = requests.get(url='http://127.0.0.1:8000/our_endpoints/server_time/')
# print(response.text)

class GetRequests:
    @classmethod
    def print_response_headers(self, response_headers):
        for key, value in response_headers.items():
            print(key, ": ", value)

    @classmethod
    def make_get_request(self, url, params=None, headers=None):
        return requests.get(url=url, params=params, headers=headers)
        if res.status_code == 200:
            self.print_response_headers(res.headers)
        else:
            self.print_response_headers(res.status_code)

# urls = {'google': 'https://www.google.com', 'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers')}}
# params_get = {'freeform': 'Something is HERE', 'test': 'test'}
# headers_get = {'content-type': 'application/json', 'test': 'test'}
# gr = GetRequests()
# resp = gr.make_get_request(urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][1], params=params_get, headers=headers_get)
# print(gr.print_response_headers(resp.headers))
# print(resp.content)
# print(resp.url)

class PostRequest:
    @classmethod
    def make_post_request(self, url, data=None, headers=None):
        return requests.post(url=url, data=data, headers=headers)

# urls = {'google': 'https://www.google.com', 'httpbin': {'url': 'https://httpbin.org', 'uri': ('get', 'response-headers', 'post')}}
# gr = GetRequests()
# pr = PostRequest()
#
# headers_post = {'User-Agent': 'My User Agent 1.0'}
# data = {'Something': 'Anything'}
# headers_post = {'User-Agent': 'Godzilla'}
# data = {'first_name': 'Ana', 'last_name': 'Storm', 'age': '24'}
# resp = pr.make_post_request(url=urls['httpbin']['url'] + '/' + urls['httpbin']['uri'][2], data=data, headers=headers_post)
#
# print(gr.print_response_headers(resp.headers))
# print("STATUS_CODE: ", resp.status_code)
# print(resp.text)
# print(resp.url)
#
# data = {'dir':'/uploads/', 'submit':'Submit'}
# files = {'file':('my_picture.jpg', open('my_picture.jpg', 'rb'))}
# r = requests.post(url, data=data, files=files)

# urls = {'google': 'https://www.google.com'}
# url = {'upload_file': 'http://127.0.0.1:8000/our_endpoints/upload_file/'}
# data = {'dir':'/', 'submit':'Submit'}
# files = {'text':('test.txt', open('test.txt', 'rb'))}
# response = requests.post(url, data=data, files=files)
# print(response.status_code)

url = {'server_time': 'http://127.0.0.1:8000/our_endpoints/server_time/'}
response = requests.get(url)
print(response.status_code)
