import time

from fastapi import APIRouter

from src.dependencies import UOWDep
from src.schemas import CreateNoteSchema, CreateTagSchema
from src.services import NoteService, TagService

notes_router = APIRouter(prefix="/api/v1", tags=["Notes "])


@notes_router.get("/")
async def root():
    return {"message": "Hello World"}


@notes_router.post("/notes")
def create_note(note: CreateNoteSchema, uow: UOWDep):
    note_id = NoteService().add_note(uow, note)
    return {"note_id": note_id}


@notes_router.get("/notes/{note_id}")
def get_notes(note_id: int):
    ...


@notes_router.patch("/notes/{note_id}")
def update_note(note_id: int):
    ...


@notes_router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    ...
