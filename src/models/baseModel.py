from abc import ABC, abstractmethod
from typing import Any

class BaseModel(ABC):
    @abstractmethod
    @classmethod
    def fromDict(cls, data:dict[str, Any]):
        pass