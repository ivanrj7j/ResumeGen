from typing import Any
from datetime import datetime
from .baseModel import BaseModel

class BasicInfo(BaseModel):
    def __init__(self, name:str, dob:str|datetime|float, email:str, phone:str, linkedIn:str=None, github:str=None):
        self.name = name
        self.dob = self.parseDate(dob)
        self.email = email
        self.phone = phone
        self.linkedIn = linkedIn
        self.github = github

    @classmethod
    def fromDict(cls, data:dict):
        return cls(data["name"], data["dob"], data["email"], data["phone"], data["linkedIn"], data["github"])

    def getDict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "dob": self.dob.strftime("%Y-%m-%d"),
            "email": self.email,
            "phone": self.phone,
            "linkedIn": self.linkedIn,
            "github": self.github
        }