tasks = []

while True:
    print("\n====== TO DO LIST ======")
    print("1. View tasks 🎑")
    print("2. Add tasks 🥸")
    print("3. Delete task 🗑️")
    print("4. Exit 👋")

    choice = input("Enter choice: ")

    # ---------------- VIEW TASKS ----------------
    if choice == "1":
        if tasks == []:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            i = 1
            for t in tasks:
                print(f"{i}. {t}")
                i += 1

    # ---------------- ADD TASKS ----------------
    elif choice == "2":
        user = input("Enter tasks separated by comma: ")
        new_tasks = user.split(",")

        for t in new_tasks:
            t = t.strip()
            if t != "":
                tasks.append(t)

        print("Tasks added!")

    # ---------------- DELETE TASK ----------------
    elif choice == "3":
        if tasks == []:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

            try:
                num = int(input("Enter task number to delete: "))

                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task deleted!")
                else:
                    print("Invalid number.")

            except ValueError:
                print("Please enter a NUMBER only.")

    # ---------------- EXIT ----------------
    elif choice == "4":
        print("GG Goodbyee 🙋")
        break

    # ---------------- WRONG INPUT ----------------
    else:
        print("Choose only 1, 2, 3 or 4.")
