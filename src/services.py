from src.schemas import NoteSchema, TagSchema, CreateTagSchema
from src.unitofwork import IUnitOfWork


class NoteService:

    def add_note(self, uow: IUnitOfWork, note: NoteSchema):
        note_dict = note.model_dump()
        with uow:
            note_id = uow.note.add_one(note_dict)
            default_tag = CreateTagSchema(tag="work")
            tag_id = uow.tag.add_one(default_tag.model_dump())
            uow.commit()
            return note_id


class TagService:
    def add_tag(self, uow: IUnitOfWork, tag: TagSchema):
        tag_dict = tag.model_dump()
        print(tag_dict)
        with uow:
            tag_id = uow.tag.add_one(tag_dict)
            uow.commit()
            return tag_id