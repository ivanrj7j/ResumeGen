from .skill import Skill

class Project:
    def __init__(self, title:str, desc:str, skillsUsed:list[Skill], url:str):
        self.title = title
        self.desc = desc
        self.skillsUsed = skillsUsed
        self.url = url
    
    @classmethod
    def fromDict(cls, data:dict):
        skills = [Skill.fromDict(s) if isinstance(s, dict) else s for s in data["skillsUsed"]]
        return cls(
            data["title"],
            data["desc"],
            skills,
            data["url"]
        )