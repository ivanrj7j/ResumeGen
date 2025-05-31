import unittest
from src.extractor import ResumeExtractor
from src.models import CandidateInfo
from dotenv import load_dotenv
import os
import base64

load_dotenv()

class ExtractorTest(unittest.TestCase):
    def test_resume(self):
        with open("prompts/extractor.md", encoding="utf-8") as f:
            prompt = f.read()

        with open("testFiles/testResume.pdf", "rb") as f:
            fileInput = f.read()

        extractor = ResumeExtractor(os.environ["GEMINI_KEY"], prompt)
        response = extractor.extract(base64.b64encode(fileInput).decode('utf-8'))
        candidate = CandidateInfo.fromJSON(response)