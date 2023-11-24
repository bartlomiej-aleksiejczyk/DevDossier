from enum import Enum


class EntryType(Enum):
    TYPE1 = "Bug"
    TYPE2 = "Feature suggestion"


class EntryStatus(Enum):
    NEW = "New"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class EntryPriority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
