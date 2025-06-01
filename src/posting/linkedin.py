import requests
from ..models import Posting
from bs4 import BeautifulSoup
from .exceptions import ParseException
from random_user_agent.user_agent import UserAgent
from .crawler import Crawler

class LinkedinCrawler(Crawler):
    """
    Crawler implementation for scraping job postings from LinkedIn job pages.

    This class extends the Crawler base class and implements the parse method to extract
    job posting details such as title, company, description, and company link from a LinkedIn job posting URL.
    """
    def parse(self) -> Posting:
        """
        Parse the current LinkedIn job posting URL and extract posting details.

        Returns:
            Posting: A Posting object containing the job title, description, company name, and company link.

        Raises:
            ParseException: If the HTTP request fails or the response status is not 200.
            Exception: For any other parsing or network errors.
        """
        if self.url is not None:
            try:
                agentGenerator = UserAgent()
                agent = agentGenerator.get_random_user_agent()
                headers = {
                    "User-Agent": agent
                }
                response = requests.get(self.url, headers=headers)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    title = soup.select_one(".topcard__title")
                    company = soup.select_one(".topcard__org-name-link")
                    desc = soup.select_one(".description__text .show-more-less-html__markup")

                    posting = Posting(title.text.strip(), desc.text.strip(), company.text.strip(), company.get("href").strip())
                    
                    return posting
                else:
                    raise ParseException(f"Got {response.status_code} from {self.url}")
            except Exception as e:
                print(e)