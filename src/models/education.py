from datetime import datetime
from typing import Any

from .baseModel import BaseModel

class Education(BaseModel):
    def __init__(self, institute:str, startDate:float|datetime, endDate:float|datetime, score:float, maxScore:float):
        self.institue = institute
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
            "institute": self.institue,
            "startDate": self.startDate.strftime("%Y-%m-%d"),
            "endDate": self.endDate.strftime("%Y-%m-%d"),
            "score": self.score,
            "maxScore": self.maxScore
        }