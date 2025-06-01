import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from datetime import datetime

from src.models import BasicInfo
from src.models import Education
from src.models import Experience
from src.models import Project
from src.models import Skill
from src.models import CandidateInfo


class TestModels(unittest.TestCase):
    def test_contact_init_and_fromDict(self):
        data = {
            "name": "John Doe",
            "dob": "2000-01-01",
            "email": "john@example.com",
            "phone": "1234567890",
            "linkedIn": "linkedin.com/in/johndoe",
            "github": "github.com/johndoe"
        }
        c = BasicInfo(**data)
        self.assertEqual(c.name, data["name"])
        self.assertEqual(c.email, data["email"])
        self.assertEqual(c.phone, data["phone"])
        self.assertEqual(c.linkedIn, data["linkedIn"])
        self.assertEqual(c.github, data["github"])
        c2 = BasicInfo.fromDict(data)
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
        contact = BasicInfo("John Doe", "2000-10-25","john@example.com", "1234567890", "linkedin.com/in/johndoe", "github.com/johndoe")
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

    def test_getDict(self):
        # Complete data
        contact = BasicInfo("John Doe", "1969-5-5", "john@example.com", "1234567890", "linkedin.com/in/johndoe", "github.com/johndoe")
        education = [Education("Test University", datetime.now(), datetime.now(), 8.5, 10.0)]
        experience = [Experience("Developer", "TestCorp", 0, datetime.now(), datetime.now(), [])]
        projects = [Project("ResumeGen", "A resume generator", [], "https://github.com/test/resumegen")]
        skills = [Skill("Python", datetime.now(), 2)]
        ci = CandidateInfo(contact, education, experience, projects, skills)
        result = ci.getDict()
        self.assertEqual(result["contact"]["name"], "John Doe")
        # Incomplete data
        contact_incomplete = BasicInfo("", "", "", "", None, None)
        education_incomplete = [Education("", "", "", None, None)]
        experience_incomplete = [Experience("", "", 0, "", "", [])]
        projects_incomplete = [Project("", "", [], "")]
        skills_incomplete = [Skill("", "", 0)]
        ci_incomplete = CandidateInfo(contact_incomplete, education_incomplete, experience_incomplete, projects_incomplete, skills_incomplete)
        result_incomplete = ci_incomplete.getDict()
        self.assertEqual(result_incomplete["contact"]["name"], "")
        self.assertEqual(result_incomplete["education"][0]["institute"], "")
        self.assertEqual(result_incomplete["experience"][0]["title"], "")
        self.assertEqual(result_incomplete["projects"][0]["title"], "")
        self.assertEqual(result_incomplete["skills"][0]["title"], "")

    def test_getJSON(self):
        # Complete data
        contact = BasicInfo("John Doe", "2006-5-5", "john@example.com", "1234567890", "linkedin.com/in/johndoe", "github.com/johndoe")
        education = [Education("Test University", datetime.now(), datetime.now(), 8.5, 10.0)]
        experience = [Experience("Developer", "TestCorp", 0, datetime.now(), datetime.now(), [])]
        projects = [Project("ResumeGen", "A resume generator", [], "https://github.com/test/resumegen")]
        skills = [Skill("Python", datetime.now(), 2)]
        ci = CandidateInfo(contact, education, experience, projects, skills)
        ci.getJSON()
        # Incomplete data
        contact_incomplete = BasicInfo("", "", "", "", None, None)
        education_incomplete = [Education("", "", "", None, None)]
        experience_incomplete = [Experience("", "", 0, "", "", [])]
        projects_incomplete = [Project("", "", [], "")]
        skills_incomplete = [Skill("", "", 0)]
        ci_incomplete = CandidateInfo(contact_incomplete, education_incomplete, experience_incomplete, projects_incomplete, skills_incomplete)
        ci_incomplete.getJSON()

    def test_incomplete_basicinfo(self):
        incomplete_data = {
            "name": "",
            "dob": "",
            "email": "john@example.com",
            "phone": "",
            "linkedIn": None,
            "github": None
        }
        c = BasicInfo.fromDict(incomplete_data)
        self.assertEqual(c.name, "")
        self.assertEqual(c.dob, None)
        self.assertEqual(c.phone, "")
        self.assertEqual(c.linkedIn, None)
        self.assertEqual(c.github, None)
        d = c.getDict()
        self.assertEqual(d["name"], "")
        self.assertEqual(d["dob"], None)

    def test_incomplete_education(self):
        incomplete_data = {
            "institute": "",
            "startDate": "",
            "endDate": "",
            "score": None,
            "maxScore": None
        }
        e = Education.fromDict(incomplete_data)
        self.assertEqual(e.institue, "")
        self.assertEqual(e.startDate, None)
        self.assertEqual(e.endDate, None)
        self.assertEqual(e.score, None)
        self.assertEqual(e.maxScore, None)
        d = e.getDict()
        self.assertEqual(d["institute"], "")
        self.assertEqual(d["startDate"], None)

    def test_incomplete_skill(self):
        incomplete_data = {
            "title": "",
            "experience": 0.0,
            "proficiency": 0
        }
        s = Skill.fromDict(incomplete_data)
        self.assertEqual(s.title, "")
        self.assertEqual(s.proficiency, 0)
        d = s.getDict()
        self.assertEqual(d["title"], "")

    def test_incomplete_project(self):
        incomplete_data = {
            "title": "",
            "desc": "",
            "skillsUsed": [],
            "url": ""
        }
        p = Project.fromDict(incomplete_data)
        self.assertEqual(p.title, "")
        self.assertEqual(p.desc, "")
        self.assertEqual(p.url, "")
        self.assertEqual(p.skillsUsed, [])
        d = p.getDict()
        self.assertEqual(d["title"], "")
        self.assertEqual(d["skillsUsed"], [])

    def test_incomplete_experience(self):
        incomplete_data = {
            "title": "",
            "company": "",
            "type": 0,
            "startDate": "",
            "endDate": "",
            "skillsUsed": []
        }
        e = Experience.fromDict(incomplete_data)
        self.assertEqual(e.title, "")
        self.assertEqual(e.company, "")
        self.assertEqual(e.type, 0)
        self.assertEqual(e.startDate, None)
        self.assertEqual(e.endDate, None)
        self.assertEqual(e.skillsUsed, [])
        d = e.getDict()
        self.assertEqual(d["title"], "")
        self.assertEqual(d["skillsUsed"], [])

    def test_incomplete_candidate_info(self):
        contact = BasicInfo("", "", "", "", None, None)
        education = [Education("", "", "", None, None)]
        experience = [Experience("", "", 0, "", "", [])]
        projects = [Project("", "", [], "")]
        skills = [Skill("", "", 0)]
        ci = CandidateInfo(contact, education, experience, projects, skills)
        d = ci.getDict()
        self.assertEqual(d["contact"]["name"], "")
        self.assertEqual(d["education"][0]["institute"], "")
        self.assertEqual(d["experience"][0]["title"], "")
        self.assertEqual(d["projects"][0]["title"], "")
        self.assertEqual(d["skills"][0]["title"], "")

if __name__ == "__main__":
    unittest.main()
