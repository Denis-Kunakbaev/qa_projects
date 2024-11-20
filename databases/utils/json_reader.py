import json


class JsonHelper:
    def __init__(self, path):
        self._data = None
        self._path = path

    def read_json(self):
        with open(self._path, 'r') as f:
            self._data = json.load(f)

    def get_data(self):
        if self._data is None:
            self.read_json()
        return self._data
