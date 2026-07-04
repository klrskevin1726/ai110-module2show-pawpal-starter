from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(title, schedule):
    print(title)
    print("-" * len(title))

    if not schedule:
        print("No tasks found.")
        return

    for pet_name, task in schedule:
        status = "Done" if task.completed else "Pending"
        print(
            f"{task.due_time} | {pet_name} | {task.title} "
            f"({task.category}) | Priority: {task.priority} | "
            f"Recurrence: {task.recurrence} | Status: {status}"
        )


def print_conflicts(conflicts):
    print("\nScheduling Conflicts")
    print("--------------------")

    if not conflicts:
        print("No conflicts found.")
        return

    for pet_name_1, task_1, pet_name_2, task_2 in conflicts:
        print(
            f"Conflict at {task_1.due_time}: "
            f"{pet_name_1}'s task '{task_1.title}' overlaps with "
            f"{pet_name_2}'s task '{task_2.title}'."
        )


def main():
    owner = Owner("Kevin")

    dog = Pet("Max", "Dog", 3)
    cat = Pet("Luna", "Cat", 2)

    dog.add_task(Task("Evening walk", "Exercise", "18:00", "medium", "daily"))
    dog.add_task(Task("Morning feeding", "Feeding", "08:00", "high", "daily"))
    cat.add_task(Task("Medication", "Medication", "08:00", "high", "daily"))
    cat.add_task(Task("Vet appointment", "Appointment", "14:30", "high", "none"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()
    scheduler.load_tasks_from_owner(owner)

    print_schedule("Sorted Schedule", scheduler.sort_by_time())
    print_schedule("\nPending Tasks", scheduler.filter_tasks(completed=False))
    print_schedule("\nTasks for Max", scheduler.filter_tasks(pet_name="Max"))

    print_conflicts(scheduler.detect_conflicts())

    print("\nCompleting Max's recurring task: Morning feeding")
    dog.mark_task_complete("Morning feeding")

    scheduler.load_tasks_from_owner(owner)
    print_schedule("\nRecurring Tasks After Completion", scheduler.get_recurring_tasks())


if __name__ == "__main__":
    main()