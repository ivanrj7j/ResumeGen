from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Literal

class Skill:
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
        self.startDate = startDate if type(startDate) == datetime else datetime.fromtimestamp(startDate) 
        self.proficiency = proficiency

    @classmethod
    def fromExperience(cls, title:str, experience:float, proficiency:int):
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
        startDate = datetime.today().timestamp() - relativedelta(year=experience)
        return cls(title, startDate, proficiency)



    @property
    def experience(self):
        return (datetime.today() - self.startDate).days / 365.25