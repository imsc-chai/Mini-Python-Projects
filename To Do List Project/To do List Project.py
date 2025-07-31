class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task_description = input("Enter the Task Description: ")
        new_task = {"task": task_description, "done": False}
        self.tasks.append(new_task)
        print("Task added successfully!\n")

    def remove_task(self):
        self.display_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Task '{removed['task']}' removed successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.\n")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["done"] else "Not yet Completed"
            print(f"{idx}. {task['task']} [{status}]")
        print()

    def mark_complete(self):
        self.display_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["done"] = True
                print(f"Task '{self.tasks[index]['task']}' marked as completed!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")


def main():
    todo = ToDoList()

    while True:
        print("========== To-Do List Menu ==========")
        print()
        print("1. Add Task")
        print()
        print("2. Remove Task")
        print()
        print("3. Display Tasks")
        print()
        print("4. Mark Task as Completed")
        print()
        print("5. Exit")
        print()
        print("=====================================")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.remove_task()
        elif choice == "3":
            todo.display_tasks()
        elif choice == "4":
            todo.mark_complete()
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()