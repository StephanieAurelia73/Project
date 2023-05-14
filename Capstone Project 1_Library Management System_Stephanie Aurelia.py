from datetime import datetime

# Collection data type to store the borrowing records
library = []

# Existing borrowing records database
borrowing_records = [
    {'id': 1, 'book': 'Narnia', 'borrower': 'Stephanie Aurelia', 'borrowed_date': datetime(2023, 4, 1), 'due_date': datetime(2023, 5, 1)},
    {'id': 2, 'book': 'The Lord of the Ring', 'borrower': 'Edward', 'borrowed_date': datetime(2023, 4, 14), 'due_date': datetime(2023, 5, 14)},
    {'id': 3, 'book': 'Harry Potter', 'borrower': 'Jessica', 'borrowed_date': datetime(2023, 4, 15), 'due_date': datetime(2023, 5, 15)},
    {'id': 4, 'book': 'To Kill a Mockingbird', 'borrower': 'Nicholas', 'borrowed_date': datetime(2023, 4, 20), 'due_date': datetime(2023, 5, 20)},
    {'id': 5, 'book': 'Kite Runner', 'borrower': 'Jennifer', 'borrowed_date': datetime(2023, 4, 25), 'due_date': datetime(2023, 5, 25)}
]


# Initialize the library with existing data
library.extend(borrowing_records)

# Function to create a new borrowing record
def create_record(record):
    library.append(record)
    print("Borrowing record created successfully.")

# Function to add new data to the library based on user input
def add_data():
    record = {}
    record['id'] = int(input("Enter ID: "))
    # Check if the ID already exists
    for existing_record in library:
        if existing_record['id'] == record['id']:
            print("Data already exists.")
            return
    record['book'] = input("Enter book name: ")
    record['borrower'] = input("Enter borrower name: ")
    borrowed_date_str = input("Enter borrowed date (YYYY-MM-DD): ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    try:
        borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d")
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        record['borrowed_date'] = borrowed_date
        record['due_date'] = due_date
        create_record(record)
        read_records()  # Display the updated records
    except ValueError:
        print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

# Function to read all borrowing records
def read_records():
    borrower = input("Enter borrower name (leave blank to display all records): ")
    
    if borrower:
        filtered_records = [record for record in library if record['borrower'] == borrower]
        
        if filtered_records:
            display_table_header()
            for record in filtered_records:
                display_record(record)
        else:
            print(f"No borrowing records found for borrower '{borrower}'.")
    else:
        if len(library) == 0:
            print("No borrowing records found.")
        else:
            display_table_header()
            for record in library:
                display_record(record)

#Function to display the table header
def display_table_header():
    print(f"{'ID':<5} {'BOOK':<25} {'BORROWER':<20} {'BORROWED DATE':<15} {'DUE DATE':<15}")
    print(f"{'-'*5} {'-'*25} {'-'*20} {'-'*15} {'-'*15}")

# Function to display a single record in the table
def display_record(record):
    print(f"{record['id']:<5} {record['book']:<25} {record['borrower']:<20} {record['borrowed_date'].strftime('%Y-%m-%d'):<15} {record['due_date'].strftime('%Y-%m-%d'):<15}")

# Function to update a borrowing record
def update_record(record_id, new_record):
    for i, record in enumerate(library):
        if record['id'] == record_id:
            library[i] = new_record
            for j, rec in enumerate(borrowing_records):
                if rec['id'] == record_id:
                    borrowing_records[j] = new_record
                    return True  # Update successful
    return False  # Update failed

# Function to delete a borrowing record
def delete_record(record_id):
    for i, record in enumerate(library):
        if record['id'] == record_id:
            del library[i]
            print("Borrowing record deleted successfully.")
            return 
    print("Borrowing record not found.")

    
# Function to display the menu options
def display_menu():
    print("Menu Selection:")
    print("1. Add new borrowing record")
    print("2. Read all borrowing records")
    print("3. Update a borrowing record")
    print("4. Delete a borrowing record")
    print("5. Exit")

# Function to handle the user's menu choice
def handle_choice(menu):
    if menu == '1':
        add_data()
    elif menu == '2':
        read_records()
    elif menu == '3':
        record_id = int(input("Enter the record ID to update: "))
        # Check if the ID exists before proceeding with the update
        if any(record['id'] == record_id for record in library):
            new_record = {}
            new_record['id'] = record_id
            new_record['book'] = input("Enter updated book name: ")
            new_record['borrower'] = input("Enter updated borrower name: ")
            borrowed_date_str = input("Enter updated borrowed date (YYYY-MM-DD): ")
            due_date_str = input("Enter updated due date (YYYY-MM-DD): ")
            try:
                borrowed_date = datetime.strptime(borrowed_date_str, "%Y-%m-%d")
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                new_record['borrowed_date'] = borrowed_date
                new_record['due_date'] = due_date
                update_record(record_id, new_record)
                read_records()  # Display the updated records
            except ValueError:
                print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
        else:
            print("Borrowing record not found.")
    elif menu == '4':
         record_id = int(input("Enter the record ID to delete: "))
         delete_record(record_id)
    elif menu == '5':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# Main program loop
while True:
    display_menu()
    user_choice = input("Enter your choice (1-5): ")
    if user_choice == '5':
        print("Exiting...")
        break  # Exit the loop
    handle_choice(user_choice)
    print()
