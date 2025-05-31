from typing import Any

from .baseModel import BaseModel
from .basicinfo import BasicInfo
from .education import Education
from .experience import Experience
from .project import Project
from .skill import Skill

class CandidateInfo(BaseModel):
    @classmethod
    def fromDict(cls, data: dict[str, Any]):
        # TODO: Create a fromDICT method
        pass

    def __init__(self, contact:BasicInfo, education:list[Education], experience:list[Experience], projects:list[Project], skills:list[Skill]):
        self.contact = contact 
        self.education = education
        self.experience = experience
        self.projects = projects
        self.skills = skills

    def getDict(self) -> dict[str, Any]:
        return {
            "contact": self.contact.getDict(),
            "education": [x.getDict() for x in self.education],
            "experience": [x.getDict() for x in self.experience],
            "projects": [x.getDict() for x in self.projects],
            "skills": [x.getDict() for x in self.skills]
        }