from interfaces.manager_library import Library
import json
from book import Book
from video import Video
from link import Link
from os.path import exists

class Libfile(Library):
    def __init__(self, config = {}):
        self.storage = list()
        self.file = config.get('file', '/storage/lib.json')
        if exists(self.file):
            f = open(self.file)
            data = json.loads(f.read())
            f.close()
            for item in data:
                if item.get('type') == 'book':
                    self.storage.append(Book(**item))
