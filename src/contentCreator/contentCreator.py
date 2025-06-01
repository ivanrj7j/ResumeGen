from ..baseAI import BaseAI
from typing import Any

class ContentCreator(BaseAI):
    def __init__(self, geminiKEY: str, prompt: str, model: str = "gemini-2.0-flash-lite"):
        super().__init__(geminiKEY, prompt, None, None, model)