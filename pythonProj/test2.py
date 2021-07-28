import requests

query = {'q': 'stream', 'order': 'length', 'min_width': '5000', 'min_height': '300'}
req = requests.get('https://flickr.com/explore/', params=query)

print(req.url)
