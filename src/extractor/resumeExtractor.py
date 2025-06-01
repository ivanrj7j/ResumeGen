from typing import Any
from .schema import *
from google.genai import types
from ..baseAI import BaseAI
import base64


class ResumeExtractor(BaseAI):
    def __init__(self, geminiKEY: str, prompt: str, schema: dict[str, Any] = schema,
                 requiredFields: list[str] = requiredFields, model: str = "gemini-2.0-flash-lite") -> None:
        super().__init__(geminiKEY, prompt, schema, requiredFields, model)

    def __extract(self, contents:list[types.Content]) -> str | None:
        return self.client.models.generate_content(
            model=self.model,
            contents=contents,
            config=self.config
        ).text

    def extract(self, file:str) -> str | None:
        content = types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type="application/pdf",
                    data=base64.b64decode(
                        file
                    ),
                ),
            ],
        )

        return self.__extract([content])
