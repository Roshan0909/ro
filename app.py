import streamlit as st

# Initialize tasks using session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# List of names for the dropdown
names = ["Nagaroshan", "Surajee Kumar", "Sathish", "Nishanth", "Vigneshwar"]

# Streamlit UI
st.set_page_config(page_title="Task Management System", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Assign Task", "View Tasks"])

# Page: Task Assignment
if page == "Assign Task":
    st.title("Assign a Task")
    task_name = st.text_input("Task Name")
    description = st.text_area("Description")
    deadline = st.date_input("Deadline")
    assigned_to = st.selectbox("Assign to", names)
    assign_button = st.button("Assign Task")

    # Task assignment logic
    if assign_button and task_name and description and deadline and assigned_to:
        task_id = len(st.session_state.tasks) + 1
        st.session_state.tasks.append({"id": task_id, "task_name": task_name, "description": description, "deadline": deadline, "assigned_to": assigned_to, "status": "Pending"})
        st.success(f"Task '{task_name}' assigned to {assigned_to} successfully!")

# Page: View Tasks
elif page == "View Tasks":
    st.title("Assigned Tasks")
    task_to_remove = None

    # List assigned tasks
    for task in st.session_state.tasks:
        st.write(f"**Task Name:** {task['task_name']}")
        st.write(f"**Description:** {task['description']}")
        st.write(f"**Deadline:** {task['deadline']}")
        st.write(f"**Assigned To:** {task['assigned_to']}")
        task_status = st.checkbox("Completed", value=(task['status'] == "Completed"))
        if task_status:
            task["status"] = "Completed"
        remove_task = st.button(f"Delete Task (ID: {task['id']})")
        if remove_task:
            task_to_remove = task['id']

    # Remove task logic
    if task_to_remove:
        st.session_state.tasks = [task for task in st.session_state.tasks if task['id'] != task_to_remove]

# Footer
st.markdown("---")
st.markdown("Task Management System developed by Your Name")
