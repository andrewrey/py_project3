from filestack import Client
from config import key


class FileSharer:
    def __init__(self, filepath, api_key=key):
        self.api_key = api_key
        self.filepath = filepath

    def upload(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
