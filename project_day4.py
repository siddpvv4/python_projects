def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
# ----------- MAIN PROGRAM (the manager) -----------
while True:
    print("\n====== WELCOME TO CALCULATOR ======")
    print("1. ADD ➕")
    print("2. SUBTRACT ➖")
    print("3. DIVIDE ➗")
    print("4. MULTIPLY ✖️")
    print("5. EXIT 🚪")
    choice = input("Enter choice: ")
    if choice == "5":
        print("GG Goodbyee 🙋")
        break

    # take numbers ONLY ONCE
    try:
        i = float(input("Enter first number: "))
        j = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    # call the correct function
    if choice == "1":
        answer = add(i, j)
    elif choice == "2":
        answer = subtract(i, j)
    elif choice == "3":
        answer = divide(i, j)
    elif choice == "4":
        answer = multiply(i, j)
    else:
        print("Choose only 1, 2, 3, 4 or 5.")
        continue

    print("The answer is:", answer)
