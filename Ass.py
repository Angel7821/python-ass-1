# To do List App in Python
tasks = []  # This will store all tasks
# Add a task
def add_task():
    title = input("Enter task title/description: ")
    task = {
        "title": title,
        'completed': False
    }
    tasks.append(task)
    print("Task added successfully!")
# View tasks
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
    print(f"{index}. {task['title']} - {status}")

# Edit a task
def edit_task():
    view_tasks()  
    try:
        task_no=int(input("Enter task number to edit: "))-1
        if 0 <= task_no < len(tasks):
            new_title = input("Enter your new Title")
            task[task_no][title] =new_title
            print('Sucessful update')
        else:
            print('Invalid input')
    except ValueError:
        print("Please enter a valid number.")
# Mark a task as completed
def mark_task():
    view_tasks()
    try:
        task_no=int(input("Enter task number to edit: "))-1
        if 0 <= task_no < len(tasks):
            mark = input('Are are sure you completed the task (yes/no)').lower()
            if mark =='yes' or 'y':
                task[task_no]['completed'] = True
                print('Task Successfully Completed')
            else:
                task[task_no]['completed'] = False
            
        else:
            print('Invalid input')
    except ValueError:
        print('Enter a valid Number')

# Delete a task
def delete_task():
    view_tasks()
try:
    task_no= int(input('Enter the number to be poppped')) -1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        print('task successfully deleted')
    else:
        print('enter valid num')
except ValueError:
    print('Invalid input')

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
