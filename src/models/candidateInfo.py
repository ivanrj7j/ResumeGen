from . import *

class CandidateInfo:
    def __init__(self, contact:Contact, education:list[Education], experience:list[Experience], projects:list[Project], skills:list[Skill]):
        self.contact = contact 
        self.education = education
        self.experience = experience
        self.projects = projects
        self.skills = skills