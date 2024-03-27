from datetime import datetime

from pydantic import BaseModel


class NoteSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    description: str
    importance: str

    class Config:
        from_attributes = True

class TagSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    tag: str


class CreateNoteSchema(BaseModel):
    description: str
    importance: str

    class Config:
        from_attributes = True


class CreateTagSchema(BaseModel):
    tag: str

    class Config:
        from_attributes = True
