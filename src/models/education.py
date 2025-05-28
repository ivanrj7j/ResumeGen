from datetime import datetime

class Education:
    def __init__(self, institute:str, startDate:float|datetime, endDate:float|datetime, score:float, maxScore:float):
        self.institue = institute
        self.startDate = startDate if type(startDate) == datetime else datetime.fromtimestamp(startDate)
        self.endDate = endDate if type(endDate) == datetime else datetime.fromtimestamp(endDate)
        self.score = score
        self.maxScore = maxScore

    @classmethod
    def fromDict(cls, data:dict):
        return cls(
            data["institute"],
            data["startDate"],
            data["endDate"],
            data["score"],
            data["maxScore"]
        )