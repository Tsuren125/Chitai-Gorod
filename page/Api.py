import requests
from data.data import HEADERS_PROJECT
import allure


class Api:

    def __init__(self, url):
        self.url = url
        self.headers = HEADERS_PROJECT

    @allure.step("Поиск книги")
    def search(self, params):
        resp = requests.get(self.url, headers=self.headers, params=params)
        return resp
