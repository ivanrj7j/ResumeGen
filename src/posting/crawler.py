from abc import ABC, abstractmethod
from ..models import Posting

class Crawler:
    def __init__(self, stack:list[str]):
        self.stack = stack
        self.updateURL()

    def updateURL(self):
        if len(self.stack) > 0:
            self.url = self.stack.pop()
        else:
            self.url = None

    @abstractmethod
    def parse(self) -> Posting:
        pass

    def __iter__(self):
        return self
    
    def __next__(self):
        self.updateURL()
        if self.url is None:
            raise StopIteration
        return self.parse()