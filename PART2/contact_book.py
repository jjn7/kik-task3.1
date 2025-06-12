import json

#Import contacts from JSON file as read only
try:
    with open("contacts.json", "r") as file:
            contacts = json.load(file)
except FileNotFoundError:
      contacts = {}

def save_contact():
      with open("contacts.json", "w") as file: #opens file with write permission
            json.dump(contacts, file, indent=2) #json.dump writes the data #indent creates nested data which is easier to read

#Add New Contact function
def add_contact ():
    name = input("Enter contact name: ")
    if name in contacts: #Check if contact exists
        print("This contact already exists")
    else:
         email = input("Enter contact email: ")
         phone = input("Enter contact phone: ")
         contacts[name] = { #Create Python Dictionary
              "email": email,
              "phone": phone
         }
         save_contact()
         print("Contact created")

#Create Contact Search function
def search_contact ():
     name = input("Enter contact name: ")
     if name in contacts:
          print("Name: ", name)
          print("Phone: ", contacts[name]["phone"])
          print("Email: ", contacts[name]["email"])
     else:
          print("Contact not found")


#Create Contact Update Function
def update_contact ():
     name = input("Enter contact name: ")
     if name in contacts:
          choice = input("What would you like to update? (email/phone/cancel)")
          if choice == 'email':
               email = input("Enter new email: ")
               contacts[name]["email"] = email
               save_contact()
               print("Contact email has been updated")
          elif choice == 'phone':
               phone = input("Enter new phone: ")
               contacts[name]["phone"] = phone
               save_contact()
               print("Contact phone number has been updated")
          else:
                print("No changes made")
     else:
            print("Contact not found")


#Create Contact Delete function
def delete_contact ():
     name = input("Enter contact name: ")
     if name in contacts:
        confirm = input("Are you sure you would like to delete this contact? (y/n): ").lower()
        if confirm == 'y':
             del contacts[name]
             save_contact()
             print("Contact deleted")
        else:
            print("Contact not removed")
     else:
        print("Contact not found")
        
#loop for user to chose next option
while True:

#display first menu items
    print("Contact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

#request user input
    operation = input("What would you like to do? (1, 2, 3, 4, 5): ")

#use selection construct to determine user input
    if operation == "1":
          add_contact()
    elif operation == "2":
          search_contact()
    elif operation == "3":
          update_contact()
    elif operation == "4":
          delete_contact()
    elif operation == "5":
          break
    else:
          print("Invalid operation, please try again")

#check if user wants to complete another action
    again = input("Do you want to continue using the contact book? (y/n): ").lower() #.lower() ensures that the letter is turned into lowercase
    if again != 'y':
        print("Okay, contacts saved. Have a nice day")
        break