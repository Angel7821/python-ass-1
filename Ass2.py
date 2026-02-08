print('Hello python')
# Simple To-Do App in Python

tasks = []  # This will store all tasks


def add_task():
    title = input("Enter task title/description: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"
        print(f"{index}. {task['title']} {status}")

def edit_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to edit: ")) - 1
        if 0 <= task_no < len(tasks):
            new_title = input("Enter new task title/description: ")
            tasks[task_no]["title"] = new_title
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark: ")) - 1
        if 0 <= task_no < len(tasks):
            choices = input("Mark as completed? (yes/no): ").lower()
            if choices == "yes" or choices == "y":
                tasks[task_no]["completed"] = True
            else:
                tasks[task_no]["completed"] = False
            print("Task status updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks.pop(task_no)
            print("Task removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n--- TO-DO APP MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task Completed/Pending")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye! Stay productive 💪")
            break
        else:
            print("Invalid choice. Please select 1-6.")


main()
