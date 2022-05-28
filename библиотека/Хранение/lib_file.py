from interfaces.manager_library import Library
import json

class Libfile(Library):
    def __init__(self, config = {}):
        self.storage = list()
        self.file = config.get('file', '/storage/lib.json')
        if exists(self.file):
            f = open(self.file)
            data = json.loads(f.read())
            print(data)
            f.close()
