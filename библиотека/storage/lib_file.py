from interfaces.manager_library import Library
import json

class Libfile(Library):
    def __init__(self, config = {}):
        self.storage = list()
        self.file = config.get('file', './library.json')
        f = open(self.file)
        data = f.read()
        f.close()
