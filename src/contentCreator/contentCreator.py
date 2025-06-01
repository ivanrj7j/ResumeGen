from ..baseAI import BaseAI
from typing import Any
import json
from google.genai import types

class ContentCreator(BaseAI):
    """
    ContentCreator is a class for generating content and prioritizing data for the resume.
    Args:
        geminiKEY (str): API key for authenticating with the Gemini AI service.
        prompt (str): The initial prompt or context for the content generation.
        model (str, optional): The model name to use for content generation. Defaults to "gemini-2.0-flash-lite".
    Methods:
        output(inp: dict[str, Any] | str) -> str:
            Generates content based on the provided input.
            Args:
                inp (dict[str, Any] | str): Input data for content generation. Can be a dictionary or a string.
            Returns:
                str: The generated content as a string.
    """

    def __init__(self, geminiKEY: str, prompt: str, model: str = "gemini-2.0-flash-lite"):
        super().__init__(geminiKEY, prompt, None, None, model)

    def output(self, inp:dict[str, Any]|str):
        """
        Generates content for the resume based on the input.
        Args:
            inp (dict[str, Any] | str): The input data to generate content from. If a dictionary is provided,
                it will be converted to a JSON string.
        Returns:
            str: The generated content as a string.
        """

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