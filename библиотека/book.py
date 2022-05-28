from interfaces.media import Media

class Book(Media):
    def __init__(self) -> None:
        self.name = None
        self.author = None
        self.year = None
    def __str__(self) -> str:
        return f'{self.name}. {self.author}. ({self.year})'
