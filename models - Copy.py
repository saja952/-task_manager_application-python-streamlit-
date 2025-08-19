class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_email(self, new_email):
        self.email = new_email

    def display_user_info(self):
        print(f"User Name: {self.name}")
        print(f"Email: {self.email}")


class Category:
    def __init__(self, name):
        self.name = name

    def rename_category(self, new_name):
        self.name = new_name

    def display_category_info(self):
        print(f"Category Name: {self.name}")


class Task:
    def __init__(self, title, description, due_date, assignee, category):
        self.title = title
        self.description = description
        self.status = "Pending"
        self.due_date = due_date
        self.assignee = assignee
        self.category = category

    def update_status(self, new_status):
        self.status = new_status

    def update_due_date(self, new_due_date):
        self.due_date = new_due_date

    def update_assignee(self, new_assignee):
        self.assignee = new_assignee

    def update_category(self, new_category):
        self.category = new_category

    def display_task_info(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Due Date: {self.due_date}")
        print(f"Assignee: {self.assignee.name}")
        print(f"Category: {self.category.name}")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks_by_status(self, status):
        return [t for t in self.tasks if t.status == status]

    def get_tasks_by_due_date(self, due_date):
        return [t for t in self.tasks if t.due_date == due_date]

    def get_tasks_by_assignee(self, assignee):
        return [t for t in self.tasks if t.assignee == assignee]

    def get_tasks_by_category(self, category):
        return [t for t in self.tasks if t.category == category]

    def display_all_tasks(self):
        for t in self.tasks:
            t.display_task_info()


    def display_task_manager_info(self):
        print(f"Total tasks: {len(self.tasks)}")


def create_user(name, email):
    return User(name, email)

def update_user_email(user, new_email):
    user.update_email(new_email)

def display_user_info(user):
    user.display_user_info()
