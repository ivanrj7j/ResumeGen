import unittest
from src.githubExtractor import GithubExtractor
import os
from dotenv import load_dotenv

load_dotenv()

class TestGithubExtractor(unittest.TestCase):
    def setUp(self):
        # Use a dummy or environment variable for the API key
        self.api_key = os.environ["API_KEY_GITHUB"]
        self.extractor = GithubExtractor(self.api_key)

    def test_get_project_detail(self):
        repo_full_name = 'ivanrj2/Pix2Pix-Image-Segmentation'
        project = self.extractor.getProjectDetail(repo_full_name)
        self.assertEqual(project.title, 'Pix2Pix-Image-Segmentation')
        self.assertIn('github.com/ivanrj2/Pix2Pix-Image-Segmentation', project.url)
        self.assertIsInstance(project.desc, str)

    def test_get_user_projects(self):
        user_name = 'ivanrj2'
        projects = list(self.extractor.getUserProjects(user_name))
        self.assertTrue(any(p.title == 'Pix2Pix-Image-Segmentation' for p in projects))