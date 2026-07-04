from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    title: str
    category: str
    due_time: str
    priority: str
    recurrence: str = "none"
    completed: bool = False

    def mark_complete(self):
        pass

    def is_due_today(self, date):
        pass

    def conflicts_with(self, other_task):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        pass

    def remove_task(self, task_title):
        pass

    def get_tasks(self):
        pass


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        pass

    def remove_pet(self, pet_name):
        pass

    def get_all_tasks(self):
        pass


@dataclass
class Scheduler:
    tasks: List[Task] = field(default_factory=list)

    def sort_tasks(self):
        pass

    def detect_conflicts(self):
        pass

    def get_today_tasks(self, date):
        pass

    def get_recurring_tasks(self, date):
        pass