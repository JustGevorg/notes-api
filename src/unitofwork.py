# https://github1s.com/cosmicpython/code/tree/chapter_06_uow
from abc import ABC, abstractmethod
from typing import Type

from src.db.database import session_maker
from src.repository import NoteRepository, TagRepository


class IUnitOfWork(ABC):
    notes: Type[NoteRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __enter__(self):
        ...

    @abstractmethod
    def __exit__(self, *args):
        ...

    @abstractmethod
    def commit(self):
        ...

    @abstractmethod
    def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = session_maker

    def __enter__(self):
        self.session = self.session_factory()

        self.note = NoteRepository(self.session)
        self.tag = TagRepository(self.session)

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
