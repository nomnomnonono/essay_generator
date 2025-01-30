import os

from litellm import completion

from .utils import load_config

config = load_config()
os.environ["OPENAI_API_KEY"] = config.api_key


def generate_essay(topic: str) -> str:
    response = completion(
        model="openai/gpt-4o-mini-2024-07-18",
        messages=[
            {"content": f"Write an essay on the topic: {topic}", "role": "user"},
        ],
    )
    essay: str = response.choices[0].message.content
    return essay
