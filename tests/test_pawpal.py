from datetime import date, timedelta

from pawpal_system import Pet, Task, Scheduler


def test_task_completion():
    task = Task("Morning feeding", "Feeding", "08:00", "high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Max", "Dog", 3)
    task = Task("Evening walk", "Exercise", "18:00", "medium")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Evening walk"


def test_sorting_correctness():
    morning_task = Task("Morning feeding", "Feeding", "08:00", "high")
    afternoon_task = Task("Vet appointment", "Appointment", "14:30", "high")
    evening_task = Task("Evening walk", "Exercise", "18:00", "medium")

    scheduler = Scheduler([
        ("Max", evening_task),
        ("Luna", afternoon_task),
        ("Max", morning_task),
    ])

    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0][1].due_time == "08:00"
    assert sorted_tasks[1][1].due_time == "14:30"
    assert sorted_tasks[2][1].due_time == "18:00"


def test_daily_recurring_task_creates_next_day_task():
    today = date.today()
    pet = Pet("Max", "Dog", 3)

    task = Task(
        "Morning feeding",
        "Feeding",
        "08:00",
        "high",
        recurrence="daily",
        due_date=today,
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1

    pet.mark_task_complete("Morning feeding")

    assert len(pet.tasks) == 2
    assert pet.tasks[0].completed is True
    assert pet.tasks[1].due_date == today + timedelta(days=1)
    assert pet.tasks[1].completed is False


def test_conflict_detection_flags_duplicate_times():
    task_1 = Task("Morning feeding", "Feeding", "08:00", "high")
    task_2 = Task("Medication", "Medication", "08:00", "high")

    scheduler = Scheduler([
        ("Max", task_1),
        ("Luna", task_2),
    ])

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert conflicts[0][1].title == "Morning feeding"
    assert conflicts[0][3].title == "Medication"