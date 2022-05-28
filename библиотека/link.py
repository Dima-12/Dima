from interfaces.media import Media

class Link(Media):
    def __init__(self) -> None:
        self.name = None
        self.url = None
    def __str__(self) -> str:
        return f'{self.name} / {self.url})'
