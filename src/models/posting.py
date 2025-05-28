class Posting:
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