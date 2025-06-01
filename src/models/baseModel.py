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
        """
        Parses the input time value and returns a corresponding datetime object. This is a helper method.
        Args:
            time (str | float | datetime): The time value to parse. Can be a string in the format "%Y-%m-%d",
                a float representing a Unix timestamp, or a datetime object.
        Returns:
            datetime | None: A datetime object representing the parsed time, or None if the input is an empty string,
                None, or 0.
        Raises:
            TypeError: If the input type is not str, float, or datetime.
        """

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
        """
        Converts a date-like object to a string in 'YYYY-MM-DD' format. This is a helper method.
        Args:
            time (datetime | Any): The input value to be converted. Can be a datetime object or any other type.
        Returns:
            str | None: The formatted date string if input is a datetime object,
            None if input is None, empty string, or 0,
            or the string representation of the input otherwise.
        """
        
        if isinstance(time, datetime):
            return time.strftime("%Y-%m-%d")
        elif time in [None, '', 0]:
            return None
        return str(time)
        
    @classmethod
    def fromDictList(cls, data:list[dict]):
        """
        Creates a list of class instances from a list of dictionaries.
        Args:
            data (list[dict]): A list of dictionaries, each representing the data for one instance.
        Returns:
            list: A list of class instances created from the provided dictionaries.
        Example:
            data = [{'name': 'Alice'}, {'name': 'Bob'}]
            instances = MyClass.fromDictList(data)
        """

        return [cls.fromDict(x) for x in data]