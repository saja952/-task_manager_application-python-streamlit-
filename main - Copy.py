import streamlit as st
from datetime import date
from models import (
    User, Category, Task, TaskManager,
    create_user, update_user_email, display_user_info
)

if 'users' not in st.session_state:
    st.session_state.users = []
if 'categories' not in st.session_state:
    st.session_state.categories = []
if 'manager' not in st.session_state:
    st.session_state.manager = TaskManager()

st.sidebar.title("Setup")

with st.sidebar.expander("Add User"):
    name = st.text_input("User Name")
    email = st.text_input("Email")
    if st.button("Create User"):
        st.session_state.users.append(create_user(name, email))
        st.success("User added!")

# Add Category
with st.sidebar.expander("Add Category"):
    cat_name = st.text_input("Category Name")
    if st.button("Create Category"):
        st.session_state.categories.append(Category(cat_name))
        st.success("Category added!")

st.title("Task Manager")

st.subheader("Add a New Task")

title = st.text_input("Task Title")
desc = st.text_area("Description")
due = st.date_input("Due Date", min_value=date.today())

if st.session_state.users and st.session_state.categories:
    assignee = st.selectbox("Assign To", st.session_state.users, format_func=lambda u: u.name)
    category = st.selectbox("Category", st.session_state.categories, format_func=lambda c: c.name)

    if st.button("Add Task"):
        task = Task(title, desc, due, assignee, category)
        st.session_state.manager.add_task(task)
        st.success("Task added successfully!")
else:
    st.warning("Please add users and categories first.")

st.subheader("Filter Tasks")
filter_type = st.selectbox("Filter by", ["None", "Status", "Due Date", "Assignee", "Category"])

if filter_type == "Status":
    status_choice = st.selectbox("Choose Status", ["Pending", "In Progress", "Completed"])
    tasks = st.session_state.manager.get_tasks_by_status(status_choice)
elif filter_type == "Due Date":
    date_choice = st.date_input("Choose Date")
    tasks = st.session_state.manager.get_tasks_by_due_date(date_choice)
elif filter_type == "Assignee":
    assignee_choice = st.selectbox("Choose Assignee", st.session_state.users, format_func=lambda u: u.name)
    tasks = st.session_state.manager.get_tasks_by_assignee(assignee_choice)
elif filter_type == "Category":
    category_choice = st.selectbox("Choose Category", st.session_state.categories, format_func=lambda c: c.name)
    tasks = st.session_state.manager.get_tasks_by_category(category_choice)
else:
    tasks = st.session_state.manager.tasks

st.subheader("All Tasks")
if tasks:
    for t in tasks:
        st.write(f"**{t.title}** - {t.status} - Due: {t.due_date} - Assigned to: {t.assignee.name} - Category: {t.category.name}")
        if st.button(f"Delete {t.title}"):
            st.session_state.manager.remove_task(t)
            st.experimental_rerun()
else:
    st.info("No tasks yet.")

st.sidebar.subheader("Statistics")
st.sidebar.write(f"Total tasks: {len(st.session_state.manager.tasks)}")
