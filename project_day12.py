import os

FILE = "students.txt"

# ---------- Utility Functions ----------

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    m1 = float(input("Enter marks in Subject 1: "))
    m2 = float(input("Enter marks in Subject 2: "))
    m3 = float(input("Enter marks in Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3
    grade = calculate_grade(percentage)

    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{m1},{m2},{m3},{total},{percentage:.2f},{grade}\n")

    print("Student record saved successfully!\n")


def view_students():
    print("\n--- All Students ---")

    if not os.path.exists(FILE):
        print("No records found.\n")
        return

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            print(f"""
Roll No   : {data[0]}
Name      : {data[1]}
Marks     : {data[2]}, {data[3]}, {data[4]}
Total     : {data[5]}
Percent   : {data[6]}%
Grade     : {data[7]}
---------------------------""")

def search_student():
    print("\n--- Search Student ---")
    roll_search = input("Enter roll number to search: ")

    found = False

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == roll_search:
                    found = True
                    print(f"""
Roll No   : {data[0]}
Name      : {data[1]}
Marks     : {data[2]}, {data[3]}, {data[4]}
Total     : {data[5]}
Percent   : {data[6]}%
Grade     : {data[7]}
""")

    if not found:
        print("Student not found.\n")


def topper():
    print("\n--- Class Topper ---")

    if not os.path.exists(FILE):
        print("No records available.\n")
        return

    max_percent = -1
    topper_data = None

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            percent = float(data[6])

            if percent > max_percent:
                max_percent = percent
                topper_data = data

    if topper_data:
        print(f"""
🏆 TOPPER 🏆
Roll No   : {topper_data[0]}
Name      : {topper_data[1]}
Percentage: {topper_data[6]}%
Grade     : {topper_data[7]}
""")


# ---------- Main Menu ----------

while True:
    print("""
====== STUDENT RESULT SYSTEM ======
1. Add Student
2. View All Students
3. Search Student
4. Show Class Topper
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        topper()
    elif choice == "5":
        print(" GG 🧮Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")

