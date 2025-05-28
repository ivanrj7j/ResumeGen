import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime

from src.models import Contact
from src.models import Education
from src.models import Experience
from src.models import Project
from src.models import Skill
from src.models import CandidateInfo


class TestModels(unittest.TestCase):
    def test_contact_init_and_fromDict(self):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "linkedIn": "linkedin.com/in/johndoe",
            "github": "github.com/johndoe"
        }
        c = Contact(**data)
        self.assertEqual(c.name, data["name"])
        self.assertEqual(c.email, data["email"])
        self.assertEqual(c.phone, data["phone"])
        self.assertEqual(c.linkedIn, data["linkedIn"])
        self.assertEqual(c.github, data["github"])
        c2 = Contact.fromDict(data)
        self.assertEqual(c2.name, data["name"])

    def test_education_init_and_fromDict(self):
        now = datetime.now().timestamp()
        data = {
            "institute": "Test University",
            "startDate": now,
            "endDate": now,
            "score": 8.5,
            "maxScore": 10.0
        }
        e = Education(**data)
        self.assertEqual(e.institue, data["institute"])
        self.assertAlmostEqual(e.score, data["score"])
        e2 = Education.fromDict(data)
        self.assertEqual(e2.institue, data["institute"])

    def test_skill_init_and_fromDict(self):
        now = datetime.now().timestamp()
        data = {
            "title": "Python",
            "experience": 2020.0,
            "proficiency": 2
        }
        s = Skill("Python", now, 2)
        self.assertEqual(s.title, "Python")
        self.assertEqual(s.proficiency, 2)
        s2 = Skill.fromDict(data)
        self.assertEqual(s2.title, data["title"])
        self.assertEqual(s2.proficiency, data["proficiency"])

    def test_project_init_and_fromDict(self):
        skill = Skill("Python", datetime.now(), 2)
        data = {
            "title": "ResumeGen",
            "desc": "A resume generator",
            "skillsUsed": [{"title": "Python", "experience": 2020.0, "proficiency": 2}],
            "url": "https://github.com/test/resumegen"
        }
        p = Project("ResumeGen", "A resume generator", [skill], "https://github.com/test/resumegen")
        self.assertEqual(p.title, data["title"])
        self.assertEqual(p.url, data["url"])
        p2 = Project.fromDict(data)
        self.assertEqual(p2.title, data["title"])
        self.assertEqual(p2.skillsUsed[0].title, "Python")

    def test_experience_init_and_fromDict(self):
        skill = Skill("Python", datetime.now(), 2)
        now = datetime.now().timestamp()
        data = {
            "title": "Developer",
            "company": "TestCorp",
            "type": 0,
            "startDate": now,
            "endDate": now,
            "skillsUsed": [{"title": "Python", "experience": 3.2, "proficiency": 2}]
        }
        exp = Experience("Developer", "TestCorp", 0, now, now, [skill])
        self.assertEqual(exp.title, data["title"])
        self.assertEqual(exp.company, data["company"])
        exp2 = Experience.fromDict(data)
        self.assertEqual(exp2.title, data["title"])
        self.assertEqual(exp2.skillsUsed[0].title, "Python")

    def test_candidate_info_init(self):
        contact = Contact("John Doe", "john@example.com", "1234567890", "linkedin.com/in/johndoe", "github.com/johndoe")
        education = [Education("Test University", datetime.now(), datetime.now(), 8.5, 10.0)]
        experience = [Experience("Developer", "TestCorp", 0, datetime.now(), datetime.now(), [])]
        projects = [Project("ResumeGen", "A resume generator", [], "https://github.com/test/resumegen")]
        skills = [Skill("Python", datetime.now(), 2)]
        ci = CandidateInfo(contact, education, experience, projects, skills)
        self.assertEqual(ci.contact.name, "John Doe")
        self.assertEqual(ci.education[0].institue, "Test University")
        self.assertEqual(ci.experience[0].title, "Developer")
        self.assertEqual(ci.projects[0].title, "ResumeGen")
        self.assertEqual(ci.skills[0].title, "Python")

if __name__ == "__main__":
    unittest.main()
