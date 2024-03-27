from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, declarative_base
from sqlalchemy import ForeignKey
from datetime import datetime

from typing import Annotated
from src.schemas import NoteSchema, TagSchema
from src.db.choices import NoteImportance, TagName

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(default=datetime.utcnow)]
updated_at = Annotated[datetime, mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)]

Base = declarative_base()

class BaseModelORM(Base):
    __abstract__ = True

    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class Note(BaseModelORM):
    __tablename__ = "note"

    description: Mapped[str] = mapped_column()
    importance: Mapped[NoteImportance]

    def to_schema(self) -> NoteSchema:
        return NoteSchema(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            description=self.description,
            importance=self.importance)


class Tag(BaseModelORM):
    __tablename__ = "tag"

    # note_id: Mapped[int | None] = mapped_column(ForeignKey("note.id", ondelete="SET NULL"))
    tag: Mapped[TagName]

    def to_schema(self) -> TagSchema:
        return TagSchema(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            note_id=self.note_id,
            tag=self.tag)
