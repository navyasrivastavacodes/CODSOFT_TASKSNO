# ==============================
# CONTACT BOOK MANAGEMENT SYSTEM
# ==============================

contacts = []


# ------------------------------
# Add Contact
# ------------------------------
def add_contact():

    print("\n===== Add Contact =====")

    name = input("Enter Name: ").strip().title()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    # Empty input checking
    if name == "" or phone == "" or email == "" or address == "":
        print("All fields are required!")
        return

    # Phone number validation
    if not phone.isdigit():
        print("Phone number should contain only digits!")
        return

    # Extra Feature 1: Prevent Duplicate Phone Numbers
    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with this phone number already exists!")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("\nContact Added Successfully!")


# ------------------------------
# View Contacts
# ------------------------------
def view_contacts():

    print("\n===== Contact List =====")

    if len(contacts) == 0:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):

        print(f"\nContact {index}")
        print("-" * 25)
        print("Name  :", contact["name"])
        print("Phone :", contact["phone"])

    # Extra Feature 2: Total Contacts
    print("\nTotal Contacts:", len(contacts))


# ------------------------------
# Search Contact
# ------------------------------
def search_contact():

    print("\n===== Search Contact =====")

    search = input("Enter Name or Phone Number: ").strip()

    found = False

    for contact in contacts:

        if (contact["name"].lower() == search.lower()
                or contact["phone"] == search):

            print("\n===== Contact Found =====")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True
            break

    if not found:
        print("Contact not found.")


# ------------------------------
# Update Contact
# ------------------------------
def update_contact():

    print("\n===== Update Contact =====")

    search = input("Enter Name or Phone Number: ").strip()

    for contact in contacts:

        if (contact["name"].lower() == search.lower()
                or contact["phone"] == search):

            print("\nCurrent Details")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            print("\nEnter New Details")

            new_name = input("New Name: ").strip().title()
            new_phone = input("New Phone Number: ").strip()
            new_email = input("New Email: ").strip()
            new_address = input("New Address: ").strip()

            # Empty checking
            if new_name == "" or new_phone == "" or new_email == "" or new_address == "":
                print("All fields are required!")
                return

            # Phone validation
            if not new_phone.isdigit():
                print("Phone number should contain only digits!")
                return

            # Duplicate phone check
            for other_contact in contacts:
                if other_contact != contact and other_contact["phone"] == new_phone:
                    print("Phone number already exists!")
                    return

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["address"] = new_address

            print("\nContact Updated Successfully!")
            return

    print("Contact not found.")


# ------------------------------
# Delete Contact
# ------------------------------
def delete_contact():

    print("\n===== Delete Contact =====")

    search = input("Enter Name or Phone Number: ").strip()

    for contact in contacts:

        if (contact["name"].lower() == search.lower()
                or contact["phone"] == search):

            # Extra Feature 3: Delete Confirmation
            confirm = input(
                "Are you sure you want to delete this contact? (Y/N): "
            ).strip().upper()

            if confirm == "Y":
                contacts.remove(contact)
                print("\nContact Deleted Successfully!")

            else:
                print("\nDeletion Cancelled.")

            return

    print("Contact not found.")


# ------------------------------
# Main Program
# ------------------------------

while True:

    print("\n" + "=" * 40)
    print("       CONTACT BOOK MANAGEMENT")
    print("=" * 40)

    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    print("=" * 40)

    choice = input("Enter Your Choice: ").strip()


    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\nInvalid Choice! Please try again.")