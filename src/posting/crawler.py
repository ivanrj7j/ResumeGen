from abc import ABC, abstractmethod
from ..models import Posting
from queue import Queue
from collections.abc import Iterable

class Crawler:
    def __init__(self, queue:Queue|Iterable):
        if isinstance(queue, Queue):
            self.queue = queue
        elif isinstance(queue, Iterable):
            self.queue = Queue()
            for x in queue:
                if not isinstance(x, str):
                    raise TypeError("The given queue must have urls.")
                self.queue.put(x)
        else:
            raise TypeError("Invalid type for queue")
        
        self.updateURL()

    def updateURL(self):
        if not self.queue.empty():
            self.url = self.queue.get()
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