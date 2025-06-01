import json
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Any

class BaseModel(ABC):
    @classmethod
    @abstractmethod
    def fromDict(cls, data:dict[str, Any]):
        """
        Generates an object of the class from the dictionary representation of the model.
        """
        pass

    @classmethod
    def fromJSON(cls, jsonData:str):
        """
        Returns an object fo the class from the dictionary representation of the model.
        """
        data = json.loads(jsonData)
        return cls.fromDict(data)

    @abstractmethod
    def getDict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model.
        """
        pass

    def getJSON(self):
        """
        Returns a JSON representation of the model.
        """
        return json.dumps(self.getDict())

    def parseDate(self, time:str|float|datetime):
        if isinstance(time, str):
            if time in [None, '', 0]:
                return None
            return datetime.strptime(time, "%Y-%m-%d")
        elif isinstance(time, float):
            return datetime.fromtimestamp(time)
        elif isinstance(time, datetime):
            return time
        else:
            raise TypeError("The given format for time is incompatible. Use a float/string/datetime object")
        
    def stringifyDate(self, time:datetime|Any) -> str|None:
        if isinstance(time, datetime):
            return time.strftime("%Y-%m-%d")
        elif time in [None, '', 0]:
            return None
        return str(time)
        
    @classmethod
    def fromDictList(cls, data:list[dict]):
        return [cls.fromDict(x) for x in data]