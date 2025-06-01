from google import genai
from google.genai import types
from typing import Any


class BaseAI:
    """
    Base class for interacting with Gemini AI models for content generation and extraction.

    This class sets up the client, model, and configuration for generating content using the Gemini API.
    It supports both structured (JSON) and unstructured (plain text) responses, and allows for schema-based validation.
    """
    def __init__(self, geminiKEY: str, prompt: str, schema: dict[str, Any] | None,
                 requiredFields: list[str] | None, model: str = "gemini-2.0-flash-lite", structured:bool=True) -> None:
        """
        Initialize the BaseAI with API key, prompt, schema, required fields, model, and response type.

        Args:
            geminiKEY (str): API key for authenticating with the Gemini AI service.
            prompt (str): The system prompt or instruction for the AI model.
            schema (dict[str, Any] | None): The schema for structured response validation (optional).
            requiredFields (list[str] | None): List of required fields for the schema (optional).
            model (str, optional): The model name to use. Defaults to "gemini-2.0-flash-lite".
            structured (bool, optional): Whether to expect a structured (JSON) response. Defaults to True.
        """

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
