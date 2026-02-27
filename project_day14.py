import os

FILENAME = "habits.txt"

# Load habits from file
def load_habits():
    habits = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                name, count = line.strip().split(",")
                habits[name] = int(count)
    return habits

# Save habits to file
def save_habits(habits):
    with open(FILENAME, "w") as file:
        for name, count in habits.items():
            file.write(f"{name},{count}\n")

# Add new habit
def add_habit(habits):
    name = input("Enter habit name: ").strip()
    if name in habits:
        print("Habit already exists!")
    else:
        habits[name] = 0
        print("Habit added successfully!")

# Mark habit as done
def mark_done(habits):
    name = input("Enter habit name to mark as done: ").strip()
    if name in habits:
        habits[name] += 1
        print("Great job! Habit marked as done ✅")
    else:
        print("Habit not found!")

# View habits
def view_habits(habits):
    if not habits:
        print("No habits added yet.")
        return
    
    print("\n--- Your Habits ---")
    total = 0
    for name, count in habits.items():
        print(f"{name} → Completed {count} times")
        total += count
    
    print(f"\nTotal completions: {total}")

# Main program
def main():
    habits = load_habits()
    
    while True:
        print("\n====== HABIT TRACKER ======")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_done(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            save_habits(habits)
            print("Progress saved. Keep building streaks 🔥")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()