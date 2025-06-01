from abc import ABC, abstractmethod
from ..models import Posting
from queue import Queue
from collections.abc import Iterable

class Crawler:
    """
    Abstract base class for web crawlers that iterate over a queue of URLs and parse postings.

    This class manages a queue of URLs (either a Queue object or an iterable of URL strings),
    and provides an iterator interface to process each URL sequentially. Subclasses must implement
    the `parse` method to define how a Posting is extracted from the current URL.
    """
    def __init__(self, queue:Queue|Iterable):
        """
        Initialize the Crawler with a queue of URLs.

        Args:
            queue (Queue | Iterable): A Queue object containing URLs or an iterable of URL strings.

        Raises:
            TypeError: If the queue is not a Queue or an iterable of strings.
        """
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
        """
        Update the current URL by retrieving the next URL from the queue.
        Sets self.url to None if the queue is empty.
        """
        if not self.queue.empty():
            self.url = self.queue.get()
        else:
            self.url = None

    @abstractmethod
    def parse(self) -> Posting:
        """
        Abstract method to parse the current URL and return a Posting object.

        Returns:
            Posting: The parsed posting from the current URL.
        """
        pass

    def __iter__(self):
        """
        Return the iterator object (self).

        Returns:
            Crawler: The iterator instance.
        """
        return self
    
    def __next__(self):
        """
        Retrieve and parse the next URL in the queue.

        Returns:
            Posting: The parsed posting from the next URL.

        Raises:
            StopIteration: If there are no more URLs to process.
        """
        if self.url is None:
            raise StopIteration
        result = self.parse()
        self.updateURL()
        return result