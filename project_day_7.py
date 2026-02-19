expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']} ({expense['category']})")
    print()


def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expense: ₹{total}\n")


def filter_by_category():
    category = input("Enter category to filter: ")
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]

    if not filtered:
        print("No expenses found in this category.\n")
        return

    for expense in filtered:
        print(f"{expense['name']} - ₹{expense['amount']}")
    print()


def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
