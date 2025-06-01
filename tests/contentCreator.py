from src.contentCreator import ContentCreator
import unittest
from dotenv import load_dotenv
import json
import os

load_dotenv()

class TestContentCreator(unittest.TestCase):
    def test_init(self):
        with open("prompts/contentCreator.md", encoding='utf-8') as f:
            prompt = f.read()
        creator = ContentCreator(os.environ["GEMINI_KEY"], prompt)

    def test_response(self):
        with open("prompts/contentCreator.md", encoding='utf-8') as f:
            prompt = f.read()

        with open("tests/posting.json") as f:
            posting = json.load(f)

        with open("tests/userData.json") as f:
            candidateInfo = json.load(f)

        inp = {
            'candidateInfo':candidateInfo,
            'posting': posting,
            'customInstructions': ''
        }

        creator = ContentCreator(os.environ["GEMINI_KEY"], prompt)
        creator.output(json.dumps(inp)) # testing input as json string
        output = creator.output(inp)        