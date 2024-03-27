from enum import Enum, auto


class NoteImportance(Enum):
    low = auto()
    middle = auto()
    high = auto()


class TagName(Enum):
    work = auto()
    study = auto()
    family = auto()
    sport = auto()
    other = auto()
