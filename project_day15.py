# Mini Student Result Management System

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


while True:
    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Add Student Result")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        marks1 = float(input("Enter marks for Subject 1: "))
        marks2 = float(input("Enter marks for Subject 2: "))
        marks3 = float(input("Enter marks for Subject 3: "))

        total = marks1 + marks2 + marks3
        percentage = total / 3
        grade = calculate_grade(percentage)

        print("\n----- RESULT -----")
        print("Name:", name)
        print("Total Marks:", total)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)

        # Save to file
        with open("student_results.txt", "a") as file:
            file.write(f"{name}, {total}, {round(percentage,2)}%, {grade}\n")

        print("\n✅ Result saved successfully!")

    elif choice == "2":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")