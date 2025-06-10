from ..baseAI import BaseAI
from ..render import Renderer
from logging import Logger
from google.genai import types
import json
import os
import re

class LatexEditor(BaseAI):
    def __init__(self, geminiKEY, prompt, model = "gemini-2.5-flash-preview-05-20", structured = True, logger:Logger=None):
        super().__init__(geminiKEY, prompt, None, None, model, structured)
        self.config.thinking_config = types.ThinkingConfig(
            thinking_budget=1000
        )

        self.renderer = Renderer(logger)

    def edit(self, template:str, details:dict|str, path:str=".", customName:str=""):
        if isinstance(details, str):
            details = json.loads(details)

        if os.path.exists(template):
            with open(template, encoding="utf-8") as f:
                template = f.read()
        
        details['latexCode'] = template

        inp = types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=json.dumps(details)
                ),
            ],
        )

        texCode = self.client.models.generate_content(
            model = self.model,
            contents=inp,
            config = self.config
        ).text

        texCode  = re.sub(r'(?<!\\)\\n(?![a-zA-Z])', '\n', texCode)

        with open("tempFile.tex", "w", encoding='utf-8') as f:
            f.write(texCode)

        self.renderer.renderFromSourceCode(texCode, path, customName)