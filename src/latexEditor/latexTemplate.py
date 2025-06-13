import re
from collections import defaultdict
from jinja2 import Template

class LatexTemplate:
    def __init__(self, content: str):
        self.content = content
        self.template = Template(content)

    @classmethod
    def fromFile(cls, filePath: str):
        with open(filePath, "r", encoding="utf-8") as f:
            return cls(f.read())

    @property
    def instances(self):
        mainKeys = ("shortText", "longText", "number", "title")
        # capture bracketed vars or for‑loops
        pattern = r"""
            {{\s*(\w+)\[(\d+)\]\s*}}        # group1=var, group2=index
        | {%\s*for\s+(\w+)\s+in\s+(\w+)\s*%}  # group3=loopVar, group4=collection
        """
        regex = re.compile(pattern, re.VERBOSE)

        counts = {key: set() for key in mainKeys}
        others = defaultdict(int)
        loopVars = set()

        for match in regex.finditer(self.content):
            varName, idx, loopVar, loopOver = match.groups()

            # loop declaration
            if loopVar:
                loopVars.add(loopVar)
                if loopOver in mainKeys:
                    counts[loopOver].add('loop')
                else:
                    others[loopOver] += 1

            # only bracketed vars, and not the loop‑variable
            elif varName and varName not in loopVars:
                if varName in mainKeys:
                    counts[varName].add(idx)       # idx is guaranteed
                else:
                    others[varName] += 1

        # convert sets → counts; others stays a dict
        for key in mainKeys:
            counts[key] = len(counts[key])
        counts["others"] = dict(others)

        return counts
    
    def render(self, **data):
        if "newLine" in data and data["newLine"] != '\n':
            raise ValueError("The data can't have a key named `newLine`")
        data["newLine"] = '\n'
        return self.template.render(**data)
    
    def getModelInput(self):
        return {
            "instances": self.instances,
            "template": self.content
        }


if __name__ == "__main__":
    import json
    # Define your LaTeX template as a raw string to preserve LaTeX formatting.
    template = r"""
\documentclass{article}
\begin{document}

\title{ {{ title[0] }} }
\maketitle

\section*{Short Texts}
{{ shortText[0] }}
{{ shortText[1] }}

\section*{Long Texts}
{{ longText[0] }}
{{ longText[1] }}

\section*{Misc Items}
\begin{itemize}
{% for item in misc %}
    \item {{ item }}
{% endfor %}
\end{itemize}

\section*{Numbers}
{{ number[0] }}, {{ number[1] }}

\end{document}
"""

    temp = LatexTemplate.fromFile("ignoreDir/test1Custom.jinja")
    # print(temp.content.replace("{{newLine}}", '\n'))

    with open("tempX.json", encoding="utf-8") as f:
        userData = json.load(f)

    with open("tempZ.json", encoding="utf-8") as f:
        data = json.load(f)

    # instances = {
    #     "shortText": 75,
    #     "longText": 3,
    #     "number": 8,
    #     "title": 1,
    #     "others": {
    #         "misc_items_0": 1,
    #         "misc_items_1": 1,
    #         "misc_items_2": 1
    #     }
    # }
    # data = {}
    # for x, y in instances.items():
    #     if isinstance(y, int):
    #         data[x] = ["x" for _ in range(y)]
    #     else:
    #         data[x] = {}
    #         for i, j in instances[x].items():
    #             data[x][i] = ["x" for _ in range(j)]

    # print(data)

            

    with open("ignoreDir/test1Custom.tex", "w", encoding="utf-8") as f:
        f.write(temp.render(**data))



    with open("tempY.json", "w", encoding="utf-8") as f:
        printData = temp.getModelInput()
        printData["data"] = userData
        c = json.dumps(printData, indent=4)
        f.write(c)
