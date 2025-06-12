from datetime import datetime
from typing import Any

from .baseModel import BaseModel

class Education(BaseModel):
    def __init__(self, institute:str, startDate:float|datetime, endDate:float|datetime, score:float, maxScore:float):
        self.institute = institute
        self.startDate = self.parseDate(startDate)
        self.endDate = self.parseDate(endDate)
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

    def getDict(self) -> dict[str, Any]:
        return {
            "institute": self.institute,
            "startDate": self.stringifyDate(self.startDate),
            "endDate": self.stringifyDate(self.endDate),
            "score": self.score,
            "maxScore": self.maxScore
        }