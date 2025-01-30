from typing import Annotated

from fastapi import FastAPI, HTTPException, Query

from .schema import EssyaResponse, RootResponse

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


@app.get("/", tags=["root"], status_code=200)
def read_root() -> RootResponse:
    return RootResponse(message="Welcome to the Essay Generator API!")


@app.get("/essay", tags=["essay"], status_code=200)
def generate_essay(
    topic: Annotated[str | None, Query(max_length=50)],
) -> EssyaResponse:
    return EssyaResponse(topic=topic, essay="This is an essay on " + topic)
