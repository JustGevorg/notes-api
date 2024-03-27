from abc import ABC, abstractmethod
from typing import Iterable, Any

from sqlalchemy import insert, select, update

from src.db.database import session_maker
from src.db.models import Note, Tag


class AbstractRepository(ABC):

    @abstractmethod
    def add_one(*args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def find_all(*args, **kwargs) -> Iterable[Any]:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session):
        self.session = session

    def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = self.session.execute(stmt)
        return res.scalar_one()

    def edit_one(self, id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = self.session.execute(stmt)
        return res.scalar_one()

    def find_all(self):
        stmt = select(self.model)
        res = self.session.execute(stmt)
        res = [row[0].to_schema() for row in res.all()]
        return res

    def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res


class NoteRepository(SQLAlchemyRepository):
    model = Note


class TagRepository(SQLAlchemyRepository):
    model = Tag
