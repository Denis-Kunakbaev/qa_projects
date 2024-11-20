import requests


class RequestManager:

    def __init__(self, api_url):
        self.__api_url = api_url

    def send_get_request(self, method, params=None):
        url = self.__api_url + method
        response = requests.get(url, params=params)
        return response

    def send_post_request(self, method=None, taken_url=None, files=None, params=None):
        url = self.__api_url + method if taken_url is None else taken_url
        response = requests.post(url, files=files, params=params)
        return response
