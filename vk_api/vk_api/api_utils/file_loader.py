import urllib3
from models.config_model import ConfigModel


class FileLoader:

    def download_file(self, filename, file_url):
        http = urllib3.PoolManager()
        response = http.request('GET', file_url, headers=ConfigModel.headers)
        with open(filename, 'wb') as f:
            f.write(response.data)
        return filename

    def load_file(self, file_path):
        with open(file_path, 'rb') as photo_file:
            return photo_file
