# To-Do App


list_of_tasks = []
def add_task(list_of_tasks):
    title = input("Enter the title of the task: ")
    list_of_tasks.append({"title": title, "status": "Incomplete"})
    print(f'Task "{title}" has been added successfully!')
for task in list_of_tasks:
    print(f'Task: {task["title"]}, Status: {task["status"]}')
def mark_task_as_complete(list_of_tasks):
    title = input("Enter the title of the task to mark as complete: ")
    for task in list_of_tasks:
        if task["title"] == title:
            task["status"] = "Complete"
            print(f'Task "{title}" has been marked as complete!')
            return
    print(f'Task "{title}" not found!')
def delete_task(list_of_tasks):
    title = input("Enter the title of the task to delete: ")
    for task in list_of_tasks:
        if task["title"] == title:
            list_of_tasks.remove(task)
            print(f'Task "{title}" has been deleted!')
            return
    print(f'Task "{title}" not found!')
def mark_task_as_incomplete(list_of_tasks):
    title = input("Enter the title of the task to mark as incomplete: ")
    for task in list_of_tasks:
        if task["title"] == title:
            task["status"] = "Incomplete"
            print(f'Task "{title}" has been marked as incomplete!')
            return
    print(f'Task "{title}" not found!')
def add_due_date(list_of_tasks):
    title = input("Enter the title of the task to add a due date: ")
    for task in list_of_tasks:
        if task["title"] == title:
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            task["due_date"] = due_date
            print(f'Due date "{due_date}" has been added to task "{title}"!')
            return
    print(f'Task "{title}" not found!')
def task_priority(list_of_tasks):
    title = input("Enter the title of the task to add a priority: ")
    for task in list_of_tasks:
        if task["title"] == title:
            priority = input("Enter the priority (High, Medium, Low): ")
            task["priority"] = priority
            print(f'Priority "{priority}" has been added to task "{title}"!')
            return
    print(f'Task "{title}" not found!')
def view_tasks(list_of_tasks):
    if len(list_of_tasks) == 0:
        print("No tasks found!")
    else:
        for task in list_of_tasks:
            title = task["title"]
            status = task["status"]
            due_date = task.get("due_date", "Not set")
            priority = task.get("priority", "Not set")
            print(f'Task: {title}, Status: {status}, Due Date: {due_date}, Priority: {priority}')
def main():
    list_of_tasks = []
    print("Welcome to the To-Do List App!")
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Mark a task as incomplete")
        print("5. Delete a task")
        print("6. Add a due date")
        print("7. Add a priority")
        print("8. Quit")
        choice = input("Enter your choice (1-5): ")
        try:
            if choice == "1":
                add_task(list_of_tasks)
            elif choice == "2":
                view_tasks(list_of_tasks)
            elif choice == "3":
                mark_task_as_complete(list_of_tasks)
            elif choice == "4":
                mark_task_as_incomplete(list_of_tasks)
            elif choice == "5":
                delete_task(list_of_tasks)
            elif choice == "6":
                add_due_date(list_of_tasks)
            elif choice == "7":
                task_priority(list_of_tasks)
            elif choice == "8":
                break
            else:
                print("Invalid choice! Please enter a number from 1 to 6.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
                print("Thank you for using the To-Do List App!")
if __name__ == "__main__":
    main()

    
        
    





            

              
            
            

            
            