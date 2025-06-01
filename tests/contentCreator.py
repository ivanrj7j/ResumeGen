from src.contentCreator import ContentCreator
import unittest
from dotenv import load_dotenv
import os

load_dotenv()

class TestContentCreator(unittest.TestCase):
    def test_init(self):
        with open("prompts/contentCreator.md", encoding='utf-8') as f:
            prompt = f.read()
        creator = ContentCreator(os.environ["GEMINI_KEY"], prompt)