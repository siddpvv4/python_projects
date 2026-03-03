import json
import os

FILE_NAME = "crm_data.json"

# ----------------------------
# Utility Functions
# ----------------------------

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ----------------------------
# Core Functions
# ----------------------------

def add_client():
    name = input("Client Name: ")
    email = input("Client Email: ")
    value = float(input("Deal Value: "))
    stage = "Lead"

    client = {
        "name": name,
        "email": email,
        "value": value,
        "stage": stage
    }

    data = load_data()
    data.append(client)
    save_data(data)

    print("✅ Client added successfully!")

def view_clients():
    data = load_data()
    if not data:
        print("No clients found.")
        return

    for i, client in enumerate(data):
        print(f"""
Client ID: {i}
Name: {client['name']}
Email: {client['email']}
Deal Value: ₹{client['value']}
Stage: {client['stage']}
----------------------------""")

def update_stage():
    data = load_data()
    view_clients()

    try:
        client_id = int(input("Enter Client ID to update: "))
        print("Stages: Lead, Contacted, Negotiation, Closed")
        new_stage = input("Enter new stage: ")

        data[client_id]["stage"] = new_stage
        save_data(data)

        print("✅ Stage updated successfully!")
    except:
        print("❌ Invalid input.")

def total_revenue():
    data = load_data()
    revenue = sum(client["value"] for client in data if client["stage"] == "Closed")
    print(f"💰 Total Closed Revenue: ₹{revenue}")

# ----------------------------
# Main Menu
# ----------------------------

def main():
    while True:
        print("""
======== MINI CRM ========
1. Add Client
2. View Clients
3. Update Deal Stage
4. Show Total Revenue
5. Exit
==========================
""")
        choice = input("Choose option: ")

        if choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            update_stage()
        elif choice == "4":
            total_revenue()
        elif choice == "5":
            print("Exiting CRM...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()