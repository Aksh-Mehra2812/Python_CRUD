# main.py
from db_handler import create_table, insert_item, get_all_items, update_item, delete_item
from models import Item

def print_menu():
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Quit")

def get_user_choice():
    return input("Enter your choice: ")

def main():
    create_table()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            insert_item(name, description)
            print("Item added successfully!\n")

        elif choice == '2':
            items = get_all_items()
            if not items:
                print("No items found.")
            else:
                for item in items:
                    print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}")
            print()

        elif choice == '3':
            item_id = input("Enter item ID to update: ")
            name = input("Enter new item name: ")
            description = input("Enter new item description: ")
            update_item(item_id, name, description)
            print("Item updated successfully!\n")

        elif choice == '4':
            item_id = input("Enter item ID to delete: ")
            delete_item(item_id)
            print("Item deleted successfully!\n")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
