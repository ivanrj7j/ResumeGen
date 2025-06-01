from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Literal, Any
from .baseModel import BaseModel

class Skill(BaseModel):
    def __init__(self, title:str, startDate:float|datetime, proficiency:Literal[0, 1, 2]):
        """
        Initializes a Skill instance for resume generation.
        Args:
            title (str): The name of the skill.
            startDate (float): timestamp for the time when the skill was aquired
            proficiency (int): The proficiency level of the skill:
                0 - Beginner
                1 - Intermediate
                2 - Master        
        """
        self.title = title
        self.startDate = self.parseDate(startDate)
        self.proficiency = proficiency

    @classmethod
    def fromExperience(cls, title:str, experience:float, proficiency:Literal[0, 1, 2]):
        """
        Initializes a Skill instance for resume generation.
        Args:
            title (str): The name of the skill.
            experience (float): The year the skill was first acquired (e.g., 2020.5 for mid-2020).
            proficiency (int): The proficiency level of the skill:
                0 - Beginner
                1 - Intermediate
                2 - Master        
        """
        startDate = datetime.today() - relativedelta(year=round(experience))
        return cls(title, startDate, proficiency)

    @classmethod
    def fromDict(cls, data:dict):
        return cls.fromExperience(
            data["title"],
            data["experience"],
            data["proficiency"]
        )

    @property
    def experience(self):
        try:
            return (datetime.today() - self.startDate).days / 365.25
        except TypeError:
            return ""

    def getDict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "experience": self.experience,
            "proficiency": self.proficiency,
        }