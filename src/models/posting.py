from .baseModel import BaseModel

class Posting(BaseModel):
    def __init__(self, title:str, about:str, company:str, companyURL:str):
        self.title = title
        self.about = about
        self.company = company
        self.companyURL = companyURL

    @classmethod
    def fromDict(cls, data:dict):
        return cls(
            data["title"],
            data["about"],
            data["company"],
            data["companyURL"]
        )
    
    def getDict(self):
        return {
            "title": self.title,
            "about": self.about,
            "company": self.company,
            "companyURL": self.companyURL
        }