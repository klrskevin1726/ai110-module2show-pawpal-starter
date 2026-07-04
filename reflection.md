# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My PawPal+ system will include four main classes: Owner, Pet, Task, and Scheduler.

The Owner class represents the pet owner using the app. It stores the owner's name and the list of pets they manage. It is responsible for adding pets and viewing the tasks related to those pets.

The Pet class represents an individual pet. It stores information such as the pet's name, species, age, and assigned care tasks. It is responsible for keeping track of the tasks connected to that specific pet.

The Task class represents a care activity, such as feeding, walking, medication, grooming, or an appointment. It stores details such as the task name, category, due time, priority, recurrence, and completion status.

The Scheduler class manages the logic for organizing tasks. It is responsible for sorting tasks by priority and time, detecting scheduling conflicts, and showing which tasks should be completed today.

Three core actions a user should be able to perform are:
1. Add a pet to the system.
2. Create a care task for a pet, such as feeding or medication.
3. View today's scheduled tasks organized by time and priority.


### Building Blocks

**Owner**
- Attributes:
  - name
  - pets

- Methods:
  - add_pet(pet)
  - remove_pet(pet_name)
  - get_all_tasks()

The Owner class stores information about the person using PawPal+. It keeps track of the pets that belong to the owner and allows the owner to manage those pets and view their care tasks.

**Pet**
- Attributes:
  - name
  - species
  - age
  - tasks

- Methods:
  - add_task(task)
  - remove_task(task_title)
  - get_tasks()

The Pet class represents each individual pet in the system. It stores basic pet information and keeps a list of care tasks connected to that pet.

**Task**
- Attributes:
  - title
  - category
  - due_time
  - priority
  - recurrence
  - completed

- Methods:
  - mark_complete()
  - is_due_today(date)
  - conflicts_with(other_task)

The Task class represents one care activity, such as feeding, walking, medication, grooming, or an appointment. It stores when the task should happen, how important it is, whether it repeats, and whether it has been completed.

**Scheduler**
- Attributes:
  - tasks

- Methods:
  - sort_tasks()
  - detect_conflicts()
  - get_today_tasks(date)
  - get_recurring_tasks(date)

The Scheduler class manages the algorithmic part of the system. It organizes tasks by time and priority, detects conflicts between tasks, and returns the tasks that should be completed on a specific day.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

My overall design did not change during this phase. After reviewing the UML and the `pawpal_system.py` skeleton, the four-class structure still made sense: Owner manages pets, Pet manages tasks, Task represents a care activity, and Scheduler organizes the tasks.

The AI review suggested that future implementation should make relationships and rules more explicit, especially how dates are handled and what counts as a scheduling conflict. I decided not to add new classes or methods yet because the current skeleton matches the UML and keeps the design simple. I will define those details during the implementation phase.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it detects conflicts only when two tasks have the exact same due date and due time. This keeps the algorithm simple and easy to understand, but it does not detect more complex conflicts such as overlapping task durations. This tradeoff is reasonable for PawPal+ because the current app only stores a single due time for each task, not a start time and end time. If the app became more advanced later, I would add task durations and check for overlapping time ranges.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested the most important behaviors in the PawPal+ system. These included marking a task as complete, adding a task to a pet, sorting tasks by time, creating a new task for a daily recurring task, and detecting conflicts when two tasks have the same time.

These tests were important because they verify that the main logic of the app works before connecting or relying on the Streamlit interface. They also help confirm that the scheduler can organize tasks correctly and warn the user when there is a scheduling conflict.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that my scheduler works correctly for the current version of PawPal+. The tests passed and covered the main expected behaviors.

If I had more time, I would test more edge cases, such as invalid time formats, pets with no tasks, completed tasks not appearing in today’s schedule, and tasks that overlap by duration instead of only having the exact same time.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?




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

I am confident that the main scheduling logic works correctly for the current project requirements. The tests verify the most important behaviors, but I would add more edge case tests later for invalid time formats, pets with no tasks, and overlapping time ranges.