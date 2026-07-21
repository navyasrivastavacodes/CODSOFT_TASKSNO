# -----------------------------------------
# To-Do List
# Helps users organize and manage their
# daily tasks efficiently.
#
# Features:
# - Create Task
# - Show Tasks
# - Edit Task
# - Remove Task
# - Task Counter
# -----------------------------------------

todo_list = []

while True:

    print("\n======================================")
    print("             TO-DO LIST")
    print("======================================")

    print("1. Create Task")
    print("2. Show Tasks")
    print("3. Edit Task")
    print("4. Remove Task")
    print("5. Exit")

    menu_choice = input("Enter your choice (1-5): ").strip()

    # ---------------- Create Task ----------------

    if menu_choice == "1":

        task = input("Enter a new task: ").strip()

        if task == "":
            print("Task cannot be empty!")

        else:
            todo_list.append(task)
            print("Task created successfully!")

    # ---------------- Show Tasks ----------------

    elif menu_choice == "2":

        if len(todo_list) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

            print(f"\nTotal Tasks: {len(todo_list)}")

    # ---------------- Edit Task ----------------

    elif menu_choice == "3":

        if len(todo_list) == 0:
            print("No tasks available to edit.")

        else:

            print("\nYour Tasks:")

            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

            task_index = int(input("Enter the task number to edit: "))

            if task_index < 1 or task_index > len(todo_list):
                print("Invalid task number!")

            else:

                edited_task = input("Enter the updated task: ").strip()

                if edited_task == "":
                    print("Task cannot be empty!")

                else:
                    todo_list[task_index - 1] = edited_task
                    print("Task updated successfully!")

    # ---------------- Remove Task ----------------

    elif menu_choice == "4":

        if len(todo_list) == 0:
            print("No tasks available to remove.")

        else:

            print("\nYour Tasks:")

            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

            task_index = int(input("Enter the task number to remove: "))

            if task_index < 1 or task_index > len(todo_list):
                print("Invalid task number!")

            else:
                todo_list.pop(task_index - 1)
                print("Task removed successfully!")

    # ---------------- Exit ----------------

    elif menu_choice == "5":

        print("Thank you for using the To-Do List!")
        break

    # ---------------- Invalid Choice ----------------

    else:

        print("Invalid choice! Please enter a number between 1 and 5.")