from pydantic import BaseModel


class RootResponse(BaseModel):
    message: str


class EssayResponse(BaseModel):
    topic: str
    essay: str
