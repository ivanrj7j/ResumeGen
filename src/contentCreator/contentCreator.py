from ..baseAI import BaseAI
from typing import Any
import json
from google.genai import types

class ContentCreator(BaseAI):
    def __init__(self, geminiKEY: str, prompt: str, model: str = "gemini-2.0-flash-lite"):
        super().__init__(geminiKEY, prompt, None, None, model)

    def output(self, inp:dict[str, Any]|str):
        if isinstance(inp, dict):
            inp = json.dumps(inp)

        content = types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=inp
                ),
            ],
        )

        return self.client.models.generate_content(
            model=self.model,
            contents=content,
            config=self.config
        ).text