from google.genai import types
from google import genai

schema = {
    "contact": genai.types.Schema(
        type=genai.types.Type.OBJECT,
        required=["name", "dob", "email", "phone", "linkedIn", "github"],
        properties={
            "name": genai.types.Schema(
                type=genai.types.Type.STRING,
            ),
            "dob": genai.types.Schema(
                type=genai.types.Type.STRING,
            ),
            "email": genai.types.Schema(
                type=genai.types.Type.STRING,
            ),
            "phone": genai.types.Schema(
                type=genai.types.Type.STRING,
            ),
            "linkedIn": genai.types.Schema(
                type=genai.types.Type.STRING,
            ),
            "github": genai.types.Schema(
                type=genai.types.Type.STRING,
            ),
        },
    ),
    "education": genai.types.Schema(
        type=genai.types.Type.ARRAY,
        items=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["institute", "startDate",
                      "endDate", "score", "maxScore"],
            properties={
                "institute": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "startDate": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "endDate": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "score": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "maxScore": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
            },
        ),
    ),
    "skills": genai.types.Schema(
        type=genai.types.Type.ARRAY,
        items=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["title", "experience", "proficiency"],
            properties={
                "title": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "experience": genai.types.Schema(
                    type=genai.types.Type.NUMBER,
                ),
                "proficiency": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["0", "1", "2"],
                ),
            },
        ),
    ),
    "experience": genai.types.Schema(
        type=genai.types.Type.ARRAY,
        items=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["title", "company", "type",
                      "startDate", "endDate", "skillsUsed"],
            properties={
                "title": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "company": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "type": genai.types.Schema(
                    type=genai.types.Type.STRING,
                    enum=["0", "1", "2"],
                ),
                "startDate": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "endDate": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "skillsUsed": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    items=genai.types.Schema(
                        type=genai.types.Type.OBJECT,
                        required=[
                            "title", "experience", "proficiency"],
                        properties={
                            "title": genai.types.Schema(
                                type=genai.types.Type.STRING,
                            ),
                            "experience": genai.types.Schema(
                                type=genai.types.Type.NUMBER,
                            ),
                            "proficiency": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                enum=["0", "1", "2"],
                            ),
                        },
                    ),
                ),
            },
        ),
    ),
    "projects": genai.types.Schema(
        type=genai.types.Type.ARRAY,
        items=genai.types.Schema(
            type=genai.types.Type.OBJECT,
            required=["title", "desc", "url", "skillsUsed"],
            properties={
                "title": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "desc": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "url": genai.types.Schema(
                    type=genai.types.Type.STRING,
                ),
                "skillsUsed": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    items=genai.types.Schema(
                        type=genai.types.Type.OBJECT,
                        required=[
                            "title", "experience", "proficiency"],
                        properties={
                            "title": genai.types.Schema(
                                type=genai.types.Type.STRING,
                            ),
                            "experience": genai.types.Schema(
                                type=genai.types.Type.NUMBER,
                            ),
                            "proficiency": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                enum=["0", "1", "2"],
                            ),
                        },
                    ),
                ),
            },
        ),
    ),
}

requiredFields = ["contact", "education", "skills", "experience", "projects"]
