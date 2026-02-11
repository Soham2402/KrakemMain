from enum import IntEnum


class BaseIntConstants(IntEnum):
    @classmethod
    def model_choices(cls):
        return [(key.value, key.name) for key in cls]


class ProcessingConstants(BaseIntConstants):
    PENDING: int = 0
    IN_PROGESS: int = 1
    PROCESSED: int = 2
    SUCCESSFUL: int = 3
    FAILED: int = 4


class ResourceProcessingConstants(BaseIntConstants):
    PENDING: int = 0
    IN_PROGESS: int = 1
    PROCESSED: int = 2
    SUCCESSFUL: int = 3
    FAILED: int = 4

    PARTIAL_SUCCESS: int = 5


class ResourceTypeConstants(BaseIntConstants):
    OTHER: int = 0
    TEXT: int = 1
    PDF: int = 2
    WORD: int = 3
