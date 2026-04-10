import re

phonebook = {}

def validate_phone_number(number):
    """Validate phone number format (10+ digits, allowing +, -, space, parentheses)"""
    # Remove common formatting characters
    cleaned = re.sub(r"[\s\-().]", "", number)
    
    # Check if it contains + and at least 10 digits
    if number.strip().startswith("+"):
        return len(cleaned) >= 10
    
    # Check if it contains at least 10 digits
    return len(cleaned) >= 10 and cleaned.isdigit()

def validate_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_contact(name, number=None, email=None, phone_type="mobile"):
    """Add contact with validation. Supports multiple numbers."""
    name = name.strip()
    
    if not name:
        print("Name is required.")
        return False
    
    # Create contact if it doesn't exist
    if name not in phonebook:
        phonebook[name] = {"numbers": {}, "email": None}
    
    # Add phone number
    if number:
        number = number.strip()
        if not validate_phone_number(number):
            print(f"Invalid phone number format: {number}")
            return False
        phonebook[name]["numbers"][phone_type] = number
        print(f"Added {phone_type} number for '{name}': {number}")
    
    # Add email
    if email:
        email = email.strip()
        if not validate_email(email):
            print(f"Invalid email format: {email}")
            return False
        phonebook[name]["email"] = email
        print(f"Added email for '{name}': {email}")
    
    if number or email:
        print(f"Contact '{name}' saved.")
        return True
    else:
        print("At least a phone number or email is required.")
        return False

def search_contact(name):
    """Search contact by exact name"""
    name = name.strip()
    
    if name not in phonebook:
        print(f"No contact found for '{name}'.")
        return
    
    contact = phonebook[name]
    print(f"\n--- {name} ---")
    
    if contact["numbers"]:
        for phone_type, number in contact["numbers"].items():
            print(f"  {phone_type.capitalize()}: {number}")
    
    if contact["email"]:
        print(f"  Email: {contact['email']}")

def delete_contact(name):
    """Delete entire contact"""
    name = name.strip()
    
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted contact '{name}'.")
    else:
        print(f"No contact found for '{name}'.")

def delete_number(name, phone_type="mobile"):
    """Delete specific number from contact"""
    name = name.strip()
    
    if name not in phonebook:
        print(f"No contact found for '{name}'.")
        return
    
    if phone_type in phonebook[name]["numbers"]:
        del phonebook[name]["numbers"][phone_type]
        print(f"Deleted {phone_type} number for '{name}'.")
    else:
        print(f"No {phone_type} number found for '{name}'.")

def partial_search(query):
    """Search by partial name"""
    query = query.strip().lower()
    matches = {name: contact for name, contact in phonebook.items() 
               if query in name.lower()}
    
    if not matches:
        print(f"No contacts match '{query}'.")
        return
    
    print(f"\nMatches for '{query}':")
    for name, contact in matches.items():
        print(f"\n--- {name} ---")
        for phone_type, number in contact["numbers"].items():
            print(f"  {phone_type.capitalize()}: {number}")
        if contact["email"]:
            print(f"  Email: {contact['email']}")

def show_all_contacts():
    """Display all contacts"""
    if not phonebook:
        print("Phonebook is empty.")
        return
    
    print("\n=== All Contacts ===")
    for name, contact in phonebook.items():
        print(f"\n--- {name} ---")
        for phone_type, number in contact["numbers"].items():
            print(f"  {phone_type.capitalize()}: {number}")
        if contact["email"]:
            print(f"  Email: {contact['email']}")

def show_menu():
    print("\n=== Phonebook Menu ===")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Delete specific number")
    print("5. Partial name search")
    print("6. Show all contacts")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            name = input("Name: ")
            number = input("Phone number (optional): ").strip()
            email = input("Email (optional): ").strip()
            
            phone_type = "mobile"
            if number:
                phone_type = input("Type (mobile/home/work) [mobile]: ").strip() or "mobile"
            
            add_contact(name, number or None, email or None, phone_type)
        
        elif choice == "2":
            search_contact(input("Name to search: "))
        
        elif choice == "3":
            delete_contact(input("Name to delete: "))
        
        elif choice == "4":
            name = input("Name: ")
            phone_type = input("Type (mobile/home/work) [mobile]: ").strip() or "mobile"
            delete_number(name, phone_type)
        
        elif choice == "5":
            partial_search(input("Partial name: "))
        
        elif choice == "6":
            show_all_contacts()
        
        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()