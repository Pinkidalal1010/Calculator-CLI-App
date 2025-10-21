import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks




def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task '{task}' added.")
    else:
        print("⚠️ Task cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"❌ Task '{removed}' removed.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")



def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
