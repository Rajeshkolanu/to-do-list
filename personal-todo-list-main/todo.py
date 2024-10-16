import json
import os

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False
    
    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data['title'], data['description'], data['category'])
        task.completed = data['completed']
        return task

# Function to save tasks to a JSON file
def save_tasks(tasks):
    try:
        # Get the current working directory
        print(f"Saving tasks to: {os.path.abspath('tasks.json')}")
        
        # Write tasks to the JSON file
        with open('tasks.json', 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
        print("\033[92mTasks successfully saved.\033[0m")  
    except Exception as e:
        print(f"\033[91mError saving tasks: {e}\033[0m")



# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        print("No tasks found, starting fresh.")
        return []
    except Exception as e:
        print(f"\033[91mError loading tasks: {e}\033[0m")
        return []

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print(f"\033[91mNo tasks available.\033[0m")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{i}. [{status}] {task.title} - {task.description} ({task.category})")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (e.g., Work, Personal, Urgent): ")
    
    new_task = Task(title, description, category)
    tasks.append(new_task)
    print(f"\033[92mTask '{title}' added.\033[0m")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
    print(f"\033[92mTask '{tasks[task_num].title}' marked as completed.\033[0m")
    

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        popped = tasks.pop(task_num)
    print(f"\033[91mTask '{popped.title}' deleted.\033[0m")


# Main function to interact with the user
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Save & Exit")
        
        choice = input("\033[95mChoose an option: \033[0m")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)  # Ensure tasks are saved before exiting
            print("\033[92mTasks saved. Exiting...\033[0m")
            break
        else:
            print(f"\033[91mInvalid option. Please try again.\033[0m")

if __name__ == '__main__':
    main()
