from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class User:
    username: str
    weight: Optional[float] = None

@dataclass
class Gym:
    name: str
    location: Optional[str] = None

@dataclass
class Machine:
    name: str
    gym: str
    notes: Optional[str] = None

@dataclass
class Set:
    weight: Optional[float]
    reps: Optional[int]
    flags: List[str] = field(default_factory = list)

@dataclass
class Exercise:
    name: str
    equipment: Optional[str]
    planned_sets: Optional[int]
    planned_reps: Optional[int]
    sets: List[Set] = field(default_factory = list)

@dataclass
class Session:
    date: str
    gym: str
    partner: Optional[str]
    split_day: Optional[str] = None
    exercises: List[Exercise] = field(default_factory = list)
    notes: Optional[str] = None

@dataclass
class SplitDay:
    name: str
    exercises: List[str]

@dataclass
class Split:
    name: str
    days: List[SplitDay] = field(default_factory = list)