import unittest
from queue import Queue
from src.posting.crawler import Crawler
from src.models.posting import Posting
from string import ascii_lowercase

class DummyCrawler(Crawler):
    def parse(self) -> Posting:
        # Return a dummy posting for testing
        return Posting("Title", "About", "Company", "http://company.com")

class TestCrawler(unittest.TestCase):
    def test_queue_with_queue_object(self):
        q = Queue()
        q.put("https://www.linkedin.com/jobs/view/4236888361/")
        crawler = DummyCrawler(q)
        self.assertEqual(crawler.url, "https://www.linkedin.com/jobs/view/4236888361/")

    def test_queue_with_iterable(self):
        urls = [
            "https://www.linkedin.com/jobs/view/4236888361/",
            "https://www.linkedin.com/jobs/view/4240631985/",
            "https://www.linkedin.com/jobs/view/4238471590",
            "https://www.linkedin.com/jobs/view/4238886450"
        ]
        crawler = DummyCrawler(urls)
        self.assertEqual(crawler.url, urls[0])
        # Next should update url to the next in the list
        next(crawler)
        self.assertEqual(crawler.url, urls[1])
        next(crawler)
        self.assertEqual(crawler.url, urls[2])
        next(crawler)
        self.assertEqual(crawler.url, urls[3])

    def test_queue_type_error(self):
        with self.assertRaises(TypeError):
            DummyCrawler(123)

    def test_parse_returns_posting(self):
        crawler = DummyCrawler(["http://a.com"])
        posting = crawler.parse()
        self.assertIsInstance(posting, Posting)

    def test_crawl_length(self):
        inp = [f"http://{x}.com" for x in ascii_lowercase]
        crawler = DummyCrawler(inp)
        totalCrawls = 0
        for x in crawler:
            totalCrawls += 1

        self.assertEqual(totalCrawls, len(inp))

class TestLinkedinCrawler(unittest.TestCase):
    def test_parse_returns_posting(self):
        from src.posting.linkedin import LinkedinCrawler
        # Use a dummy subclass to avoid real HTTP requests in unit tests
        class DummyLinkedinCrawler(LinkedinCrawler):
            def parse(self):
                # Simulate a parsed posting
                return Posting("LinkedIn Title", "LinkedIn About", "LinkedIn Company", "https://company.com")
        urls = [
            "https://www.linkedin.com/jobs/view/4236888361/",
            "https://www.linkedin.com/jobs/view/4240631985/"
        ]
        crawler = DummyLinkedinCrawler(urls)
        posting = crawler.parse()
        self.assertIsInstance(posting, Posting)
        self.assertEqual(posting.title, "LinkedIn Title")
        self.assertEqual(posting.company, "LinkedIn Company")

if __name__ == "__main__":
    unittest.main()
