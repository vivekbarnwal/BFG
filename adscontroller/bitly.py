import requests
import json

class Bitly():
    def __init__(self):
	    print('Constructor of Bitly class...')
    def getShortenUrl(self, longUrl):
        # link = input("Enter url: ")
        query_params = {'access_token': '031c686e86945ee707bd8c48e132f67803a29363', 'longUrl': longUrl}
        endpoint = 'https://api-ssl.bitly.com/v3/shorten'
        response = requests.get(endpoint, params=query_params, verify=False)
        data = json.loads(response.content)
        return (data['data']['url'])
