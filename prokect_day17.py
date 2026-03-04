expenses = {}

n = int(input("How many expenses? "))

for _ in range(n):
    category = input("Category: ")
    amount = float(input("Amount: "))
    
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

print("\nExpense Summary:")
total = 0

for cat, amt in expenses.items():
    print(cat, ":", amt)
    total += amt

print("Total Expense:", total)