from typing import Annotated

from fastapi import FastAPI, Query
from fastapi.exceptions import HTTPException

from .db import EssayDB
from .llm import generate_essay
from .schema import EssayResponse, RootResponse

openapi_tags = [
    {
        "name": "root",
        "description": "Operations related to the root of the API",
    },
    {
        "name": "essay",
        "description": "Operations related to generating essays",
    },
]

app = FastAPI(
    title="Essay Generator",
    description="Generate essays on any topic by ChatGPT",
    version="1.0.0",
    contact={
        "name": "nomnomnonono",
    },
    openapi_tags=openapi_tags,
)
db = EssayDB()


@app.get("/", tags=["root"], status_code=200)
def read_root() -> RootResponse:
    return RootResponse(message="Welcome to the Essay Generator API!")


@app.post("/essay", tags=["essay"], status_code=200)
def post_essay(
    topic: Annotated[str, Query(max_length=50)],
) -> EssayResponse:
    if db.get_essay(topic):
        essay = db.get_essay(topic)
    else:
        essay = generate_essay(topic)
        db.add_essay(topic, essay)
    return EssayResponse(topic=topic, essay=essay)


@app.get("/essay", tags=["essay"], status_code=200)
def get_essay(
    topic: Annotated[str, Query(max_length=50)],
) -> EssayResponse:
    essay = db.get_essay(topic)
    if essay is None:
        raise HTTPException(status_code=404, detail="Essay not found")
    return EssayResponse(topic=topic, essay=essay)
