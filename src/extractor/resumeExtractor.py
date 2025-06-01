from typing import Any
from .schema import *
from google.genai import types
from ..baseAI import BaseAI
import base64


class ResumeExtractor(BaseAI):
    """
    ResumeExtractor is a class for extracting structured information from resume files using an AI model.
    Args:
        geminiKEY (str): API key for accessing the Gemini AI model.
        prompt (str): The prompt to guide the extraction process.
        schema (dict[str, Any], optional): The schema defining the structure of the extracted data. Defaults to `schema`.
        requiredFields (list[str], optional): List of required fields to extract. Defaults to `requiredFields`.
        model (str, optional): The model name to use for extraction. Defaults to "gemini-2.0-flash-lite".
    Methods:
        extract(file: str) -> str | None:
            Extracts structured information from a base64-encoded PDF file string.
            Args:
                file (str): Base64-encoded string of the PDF file.
            Returns:
                str | None: The extracted information as a string, or None if extraction fails.
    """

    def __init__(self, geminiKEY: str, prompt: str, schema: dict[str, Any] = schema,
                 requiredFields: list[str] = requiredFields, model: str = "gemini-2.0-flash-lite") -> None:
        super().__init__(geminiKEY, prompt, schema, requiredFields, model)

    def __extract(self, contents:list[types.Content]) -> str | None:
        """
        Extracts and returns generated text content from the provided list of Content objects using the specified model and configuration.
        Args:
            contents (list[types.Content]): A list of Content objects to be processed by the model.
        Returns:
            str | None: The generated text content as a string, or None if no content is generated.
        """
        
        return self.client.models.generate_content(
            model=self.model,
            contents=contents,
            config=self.config
        ).text

    def extract(self, file:str) -> str | None:
        """
        Extracts text content from a given PDF file.
        Args:
            file (str): A base64-encoded string representing the PDF file.
        Returns:
            str | None: The extracted text content if successful, otherwise None.
        """

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
