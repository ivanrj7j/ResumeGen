from abc import ABC, abstractmethod
from typing import Any

class BaseModel(ABC):
    @classmethod
    @abstractmethod
    def fromDict(cls, data:dict[str, Any]):
        pass