from typing import Any
from .schema import *
from google import genai
from google.genai import types
import base64


class ResumeExtractor:
    def __init__(self, geminiKEY: str, prompt: str, schema: dict[str, Any] = schema,
                 requiredFields: list[str] = requiredFields, model: str = "gemini-2.0-flash-lite") -> None:
        self.client = genai.Client(api_key=geminiKEY)
        self.model = model
        self.config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=genai.types.Schema(
                type=genai.types.Type.OBJECT,
                required=requiredFields,
                properties=schema,
            ),
            system_instruction=[
                types.Part.from_text(text=prompt),
            ],
        )

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
