def main():
    tasks = []

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. see your Tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            tasks.append({"task": task_description, "done": False})
            print("Task added successfully!")

        elif choice == '2':
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    status = "✓" if task["done"] else "✗"
                    print(f"{idx}. [{status}] {task['task']}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done.")
            else:
                try:
                    task_number = int(input("Enter the task number to mark as done: "))
                    if 1 <= task_number <= len(tasks):
                        tasks[task_number - 1]["done"] = True
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting the To-Do List application. Have a good time!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()




