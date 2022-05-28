from interfaces.media import Media

class Video(Media):
    def __init__(self) -> None:
        self.name = None
        self.author = None
        self.dur = None
    def __str__(self) -> str:
        return f'{self.name}. {self.author}. ({self.dur})'
