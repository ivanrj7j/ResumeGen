from datetime import datetime
from typing import Literal
from .skill import Skill
from .baseModel import BaseModel

class Experience(BaseModel):
    def __init__(self, title:str, company:str, _type:Literal[0, 1, 2], startDate:float|datetime, endDate:float|datetime, skillsUsed:list[Skill]):
        """
        Initializes an Experience object.
        Args:
            title (str): The job or position title.
            company (str): The name of the company or organization.
            _type (Literal[0, 1, 2]): The type of experience. 
                0 for job, 1 for internship, 2 for other.
            startDate (float | datetime): The start date of the experience, as a UNIX timestamp or datetime object.
            endDate (float | datetime): The end date of the experience, as a UNIX timestamp or datetime object.
        """
        
        self.title = title
        self.company = company
        self.type = _type
        self.startDate = startDate if type(startDate) == datetime else datetime.fromtimestamp(startDate)
        self.endDate = endDate if type(endDate) == datetime else datetime.fromtimestamp(endDate)
        self.skillsUsed = skillsUsed

    @property
    def duration(self):
        end = datetime.today() if self.endDate == -1 else self.endDate
        return end - self.startDate

    @classmethod
    def fromDict(cls, data:dict):
        skills = [Skill.fromDict(s) if isinstance(s, dict) else s for s in data["skillsUsed"]]
        return cls(
            data["title"],
            data["company"],
            data["type"],
            data["startDate"],
            data["endDate"],
            skills
        )