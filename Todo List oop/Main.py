from Manager import Manager

def main():
    manager = Manager()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Display All Tasks")
        print("4. Task Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_id = input("Enter task ID (must be numeric): ")
            try:
                manager.add_task(title, description, task_id)
                print("Task added successfully.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            task_id = input("Enter task ID to mark as done: ")
            try:
                manager.mark_task_done(task_id)
                print(f"Task {task_id} marked as done.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            print("\nAll Tasks:")
            print(manager.display_tasks())

        elif choice == "4":
            print("\nTask Summary:")
            print(manager.task_summary())

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
