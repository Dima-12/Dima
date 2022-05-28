from interfaces.media import Media
class Manager:
    def __init__(self, obg) -> None:
        self.obg = obg

    def add(self) -> None:
        pass
    def update(self) -> None:
        pass

class Library:
    def list(self):
        pass
    def add(self):
        pass
    def update(self, id):
        pass
    def delete(self, id):
        pass
    def find(self, query):
        pass