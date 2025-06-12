import json

#Import contacts from JSON file
try:
    with open("contacts.json", "r") as file:
            contacts = json.load(file)
except FileNotFoundError:
      contacts = {}