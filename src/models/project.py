from .skill import Skill

class Project:
    def __init__(self, title:str, desc:str, skillsUsed:list[Skill], url:str):
        self.title = title
        self.desc = desc
        self.skillsUsed = skillsUsed
        self.url = url