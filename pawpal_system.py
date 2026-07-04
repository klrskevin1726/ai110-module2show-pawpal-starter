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
        """Mark this task as completed."""
        self.completed = True

    def is_due_today(self, date=None):
        """Return True if this task should appear in today's schedule."""
        return not self.completed

    def conflicts_with(self, other_task):
        """Return True if two tasks have the same due time."""
        return self.due_time == other_task.due_time


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task_title):
        """Remove a task from this pet by title."""
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def get_tasks(self):
        """Return all tasks assigned to this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name):
        """Remove a pet from this owner by name."""
        self.pets = [pet for pet in self.pets if pet.name != pet_name]

    def get_all_tasks(self):
        """Return all tasks from all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet.name, task))

        return all_tasks


@dataclass
class Scheduler:
    tasks: List[tuple] = field(default_factory=list)

    def load_tasks_from_owner(self, owner):
        """Load all pet tasks from an owner."""
        self.tasks = owner.get_all_tasks()

    def sort_tasks(self):
        """Sort tasks by time and priority."""
        priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

        return sorted(
            self.tasks,
            key=lambda item: (
                item[1].due_time,
                priority_order.get(item[1].priority.lower(), 4)
            )
        )

    def detect_conflicts(self):
        """Find tasks that happen at the same time."""
        conflicts = []
        sorted_tasks = self.sort_tasks()

        for i in range(len(sorted_tasks)):
            for j in range(i + 1, len(sorted_tasks)):
                pet_name_1, task_1 = sorted_tasks[i]
                pet_name_2, task_2 = sorted_tasks[j]

                if task_1.conflicts_with(task_2):
                    conflicts.append((pet_name_1, task_1, pet_name_2, task_2))

        return conflicts

    def get_today_tasks(self, date=None):
        """Return today's incomplete tasks in schedule order."""
        today_tasks = []

        for pet_name, task in self.tasks:
            if task.is_due_today(date):
                today_tasks.append((pet_name, task))

        return sorted(
            today_tasks,
            key=lambda item: item[1].due_time
        )

    def get_recurring_tasks(self, date=None):
        """Return tasks that repeat."""
        recurring_tasks = []

        for pet_name, task in self.tasks:
            if task.recurrence.lower() != "none":
                recurring_tasks.append((pet_name, task))

        return recurring_tasks