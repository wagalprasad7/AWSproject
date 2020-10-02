import requests
import json

api_key = 'kio8bSiQ04OWvyZeCbfcUlN_p5O3zWExvolwgfdZtsankcBat7BckG9GfMuHOovjxWtKbRWkjbUdqghsx2cR09VCjjYMWsSShB9yKSvASozXsPa3q281yMxelf12X3Yx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'
params = {'term':'bookstore','location':'New York City'}

req = requests.get(url, params=params, headers=headers)

parsed = json.loads(req.text)

print(parsed)