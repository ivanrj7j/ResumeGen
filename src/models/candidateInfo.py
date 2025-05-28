from .contact import Contact
from .education import Education
from .experience import Experience
from .project import Project
from .skill import Skill

class CandidateInfo:
    def __init__(self, contact:Contact, education:list[Education], experience:list[Experience], projects:list[Project], skills:list[Skill]):
        self.contact = contact 
        self.education = education
        self.experience = experience
        self.projects = projects
        self.skills = skills