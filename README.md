# PawPal+

PawPal+ is a smart pet care management system that helps pet owners organize daily care tasks for their pets. The app allows users to add pets, schedule tasks, view today's schedule, filter tasks, and detect scheduling conflicts.

## Features

- Add pets with name, species, and age.
- Schedule care tasks for each pet.
- Track task details such as category, due time, priority, recurrence, and completion status.
- View a sorted daily schedule.
- Filter tasks by pet or completion status.
- Detect scheduling conflicts when two tasks are scheduled at the same time.
- Automatically create the next occurrence for recurring daily or weekly tasks.
- Use a Streamlit interface connected to a Python object-oriented backend.

## System Architecture

The core logic is built in `pawpal_system.py` using four main classes:

- `Owner`: Manages multiple pets and provides access to all pet tasks.
- `Pet`: Stores pet details and a list of assigned tasks.
- `Task`: Represents a single care activity with time, priority, recurrence, and completion status.
- `Scheduler`: Organizes tasks, sorts them by time, filters them, detects conflicts, and retrieves recurring tasks.

The final UML diagram is stored in:

```txt
diagrams/uml_final.md
```

## Demo Walkthrough

A user can use PawPal+ by following this workflow:

1. Add a pet by entering the pet's name, species, and age.
2. Schedule a task for that pet, such as feeding, walking, medication, grooming, or an appointment.
3. View today's schedule in a table sorted by time.
4. Filter the schedule by pet or task status.
5. Check the conflict warning section to see whether two tasks are scheduled at the same time.

Example workflow:

```txt
Add pet → Schedule task → View today's schedule → Filter tasks → Check conflicts
```

## Smarter Scheduling

PawPal+ includes a smarter scheduling layer with several algorithmic features:

| Feature | Method | Description |
|---|---|---|
| Sorting by time | `Scheduler.sort_by_time()` | Returns tasks in chronological order based on due time. |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks by pet name or completion status. |
| Conflict detection | `Scheduler.detect_conflicts()` | Finds tasks scheduled for the same date and time. |
| Recurring tasks | `Task.create_next_occurrence()` | Creates the next daily or weekly task after a recurring task is completed. |
| Owner task loading | `Scheduler.load_tasks_from_owner()` | Loads all tasks from an owner's pets into the scheduler. |

## Sample CLI Output

```txt
Sorted Schedule
---------------
08:00 | Max | Morning feeding (Feeding) | Priority: high | Recurrence: daily | Status: Pending
08:00 | Luna | Medication (Medication) | Priority: high | Recurrence: daily | Status: Pending
14:30 | Luna | Vet appointment (Appointment) | Priority: high | Recurrence: none | Status: Pending
18:00 | Max | Evening walk (Exercise) | Priority: medium | Recurrence: daily | Status: Pending

Pending Tasks
-------------
08:00 | Max | Morning feeding (Feeding) | Priority: high | Recurrence: daily | Status: Pending
08:00 | Luna | Medication (Medication) | Priority: high | Recurrence: daily | Status: Pending
14:30 | Luna | Vet appointment (Appointment) | Priority: high | Recurrence: none | Status: Pending
18:00 | Max | Evening walk (Exercise) | Priority: medium | Recurrence: daily | Status: Pending

Tasks for Max
-------------
08:00 | Max | Morning feeding (Feeding) | Priority: high | Recurrence: daily | Status: Pending
18:00 | Max | Evening walk (Exercise) | Priority: medium | Recurrence: daily | Status: Pending

Scheduling Conflicts
--------------------
Conflict at 08:00: Max's task 'Morning feeding' overlaps with Luna's task 'Medication'.

Completing Max's recurring task: Morning feeding

Recurring Tasks After Completion
--------------------------------
18:00 | Max | Evening walk (Exercise) | Priority: medium | Recurrence: daily | Status: Pending
08:00 | Max | Morning feeding (Feeding) | Priority: high | Recurrence: daily | Status: Done
08:00 | Max | Morning feeding (Feeding) | Priority: high | Recurrence: daily | Status: Pending
08:00 | Luna | Medication (Medication) | Priority: high | Recurrence: daily | Status: Pending
```

## Testing PawPal+

To verify the PawPal+ system, I used `pytest` to test the core scheduling behavior.

The test suite covers:

- Task completion
- Adding tasks to pets
- Sorting tasks in chronological order
- Creating the next occurrence for daily recurring tasks
- Detecting scheduling conflicts when two tasks have the same time

Command used to run tests:

```bash
py -m pytest
```

Successful test output:

```txt
collected 5 items

tests\test_pawpal.py .....                                              [100%]

5 passed
```

Confidence Level: 4/5 stars

I am confident that the main scheduling logic works correctly for the current project requirements. The tests verify the most important behaviors, but I would add more edge case tests later for invalid time formats, pets with no tasks, completed tasks not appearing in today's schedule, and overlapping time ranges.

## How to Run

Install dependencies:

```bash
py -m pip install -r requirements.txt
```

Run the Streamlit app:

```bash
py -m streamlit run app.py
```

Run the CLI demo:

```bash
py main.py
```

Run tests:

```bash
py -m pytest
```