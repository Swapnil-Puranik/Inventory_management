#Inventory Manager Program - Externship Project using Data Structures

# Step 1: Create the inventory
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

# Function to display the current inventory
def display_inventory():
    print("\nCurrent inventory:")
    for item, (qty, price) in inventory.items():
        print("Item:",item,",Quantity:",qty,"Price:$",price)
    print()

# Function to calculate total inventory value
def total_value():
    val_tuple=inventory.values()
    total = sum(qty * price for qty, price in val_tuple)
    print("Total value of inventory: $",total)

# Main program starts
print("Welcome to the Inventory Manager!")

while True:
    display_inventory()
    print("Choose an action:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Show total value")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name to add: ").lower()
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: $"))
        inventory[name] = (qty, price)
        print(name,"added successfully!")

    elif choice == "2":
        name = input("Enter item name to remove: ").lower()
        if name in inventory:
            del inventory[name]
            print(name,"removed from inventory.")
        else:
            print("Item not found!")

    elif choice == "3":
        name = input("Enter item name to update: ").lower()
        if name in inventory:
            qty = int(input("Enter new quantity: "))
            price = float(input("Enter new price: $"))
            inventory[name] = (qty, price)
            print(name,"updated successfully!")
        else:
            print("Item not found!")

    elif choice == "4":
        total_value()

    elif choice == "5":
        print("Exiting Inventory Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
