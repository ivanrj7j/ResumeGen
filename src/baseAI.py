from google import genai
from google.genai import types
from typing import Any


class BaseAI:
    def __init__(self, geminiKEY: str, prompt: str, schema: dict[str, Any] | None,
                 requiredFields: list[str] | None, model: str = "gemini-2.0-flash-lite", structured:bool=True) -> None:

        responseSchema = genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=requiredFields,
            properties=schema,
        ) if schema is not None else None

        self.client = genai.Client(api_key=geminiKEY)
        self.model = model
        self.config = types.GenerateContentConfig(
            response_mime_type="application/json" if structured else 'text/plain',
            response_schema=responseSchema,
            system_instruction=[
                types.Part.from_text(text=prompt),
            ],
        )
