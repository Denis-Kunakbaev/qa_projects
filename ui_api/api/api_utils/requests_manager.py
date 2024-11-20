import requests


class RequestManager:

    def __init__(self, api_url):
        self.__api_url = api_url

    def send_request(self, method, params=None, json=None):
        url = self.__api_url + method
        if json is None:
            response = requests.post(url, params=params)
        else:
            response = requests.post(url, json=json)
        return response
