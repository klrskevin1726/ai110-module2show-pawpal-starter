from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Task:
    title: str
    category: str
    due_time: str
    priority: str
    recurrence: str = "none"
    due_date: date = field(default_factory=date.today)
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def is_due_today(self, current_date=None):
        """Return True if the task is due today and not completed."""
        if current_date is None:
            current_date = date.today()

        return self.due_date == current_date and not self.completed

    def conflicts_with(self, other_task):
        """Return True if two tasks happen on the same date and time."""
        return (
            self.due_date == other_task.due_date
            and self.due_time == other_task.due_time
            and not self.completed
            and not other_task.completed
        )

    def create_next_occurrence(self):
        """Create the next version of a recurring task."""
        if self.recurrence.lower() == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.recurrence.lower() == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            title=self.title,
            category=self.category,
            due_time=self.due_time,
            priority=self.priority,
            recurrence=self.recurrence,
            due_date=next_date,
        )


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

    def mark_task_complete(self, task_title):
        """Complete a task and create the next occurrence if recurring."""
        for task in self.tasks:
            if task.title == task_title and not task.completed:
                task.mark_complete()
                next_task = task.create_next_occurrence()

                if next_task:
                    self.tasks.append(next_task)

                return True

        return False


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

    def sort_by_time(self):
        """Sort tasks by due time in HH:MM format."""
        return sorted(self.tasks, key=lambda item: item[1].due_time)

    def sort_tasks(self):
        """Sort tasks by time and priority."""
        priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3,
        }

        return sorted(
            self.tasks,
            key=lambda item: (
                item[1].due_time,
                priority_order.get(item[1].priority.lower(), 4),
            ),
        )

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        filtered_tasks = self.tasks

        if pet_name:
            filtered_tasks = [
                (name, task)
                for name, task in filtered_tasks
                if name.lower() == pet_name.lower()
            ]

        if completed is not None:
            filtered_tasks = [
                (name, task)
                for name, task in filtered_tasks
                if task.completed == completed
            ]

        return filtered_tasks

    def detect_conflicts(self):
        """Find tasks that happen at the same date and time."""
        conflicts = []
        sorted_tasks = self.sort_tasks()

        for i in range(len(sorted_tasks)):
            for j in range(i + 1, len(sorted_tasks)):
                pet_name_1, task_1 = sorted_tasks[i]
                pet_name_2, task_2 = sorted_tasks[j]

                if task_1.conflicts_with(task_2):
                    conflicts.append((pet_name_1, task_1, pet_name_2, task_2))

        return conflicts

    def get_today_tasks(self, current_date=None):
        """Return today's incomplete tasks in schedule order."""
        if current_date is None:
            current_date = date.today()

        today_tasks = []

        for pet_name, task in self.tasks:
            if task.is_due_today(current_date):
                today_tasks.append((pet_name, task))

        return sorted(today_tasks, key=lambda item: item[1].due_time)

    def get_recurring_tasks(self, current_date=None):
        """Return tasks that repeat daily or weekly."""
        recurring_tasks = []

        for pet_name, task in self.tasks:
            if task.recurrence.lower() != "none":
                recurring_tasks.append((pet_name, task))

        return recurring_tasks