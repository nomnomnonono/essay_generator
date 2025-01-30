from pydantic import BaseModel


class RootResponse(BaseModel):
    message: str


class EssyaResponse(BaseModel):
    topic: str
    essay: str
