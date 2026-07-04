import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler


st.title("PawPal+ Pet Care Manager")

# Initialize app memory
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Pet Owner")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()


owner = st.session_state.owner
scheduler = st.session_state.scheduler


st.header("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name")
    species = st.text_input("Species")
    age = st.number_input("Age", min_value=0, step=1)

    submitted_pet = st.form_submit_button("Add Pet")

    if submitted_pet:
        if pet_name and species:
            new_pet = Pet(pet_name, species, age)
            owner.add_pet(new_pet)
            st.success(f"{pet_name} was added successfully!")
        else:
            st.error("Please enter a pet name and species.")


st.header("Schedule a Task")

if not owner.pets:
    st.info("Add a pet before scheduling a task.")
else:
    pet_options = [pet.name for pet in owner.pets]

    with st.form("add_task_form"):
        selected_pet_name = st.selectbox("Choose a pet", pet_options)
        task_title = st.text_input("Task title")
        category = st.selectbox(
            "Category",
            ["Feeding", "Exercise", "Medication", "Grooming", "Appointment", "Other"]
        )
        due_time = st.text_input("Due time", placeholder="Example: 08:00")
        priority = st.selectbox("Priority", ["high", "medium", "low"])
        recurrence = st.selectbox("Recurrence", ["none", "daily", "weekly"])

        submitted_task = st.form_submit_button("Add Task")

        if submitted_task:
            if task_title and due_time:
                selected_pet = None

                for pet in owner.pets:
                    if pet.name == selected_pet_name:
                        selected_pet = pet

                if selected_pet:
                    new_task = Task(
                        task_title,
                        category,
                        due_time,
                        priority,
                        recurrence
                    )
                    selected_pet.add_task(new_task)
                    st.success(f"Task '{task_title}' was added for {selected_pet_name}!")
            else:
                st.error("Please enter a task title and due time.")


st.header("Today's Schedule")

scheduler.load_tasks_from_owner(owner)
today_tasks = scheduler.get_today_tasks()

if not today_tasks:
    st.info("No tasks scheduled yet.")
else:
    for pet_name, task in today_tasks:
        status = "Done" if task.completed else "Pending"

        st.write(
            f"**{task.due_time}** | {pet_name} | {task.title} "
            f"({task.category}) | Priority: {task.priority} | Status: {status}"
        )


st.header("Scheduling Conflicts")

conflicts = scheduler.detect_conflicts()

if not conflicts:
    st.success("No scheduling conflicts found.")
else:
    for pet_name_1, task_1, pet_name_2, task_2 in conflicts:
        st.warning(
            f"Conflict at {task_1.due_time}: "
            f"{pet_name_1}'s task '{task_1.title}' overlaps with "
            f"{pet_name_2}'s task '{task_2.title}'."
        )