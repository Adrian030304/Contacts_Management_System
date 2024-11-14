import json

def add_person() -> dict[str:str] :
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name":name,
        "age":age,
        "email":email
    }
    return person

def display_people(people: list[str]):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people: list[str]):
    display_people(people)
    
    while True:    
        number_to_delete = input("Enter a number to delete: ")
        try:
            number = int(number_to_delete)
            if number <= 0 or number > len(people):
                print("Invalid number. Out of range")
            else:
                break 
        except:
            print("Invalid number")
    people.pop(number - 1)
    print("Person deleted.")
    
def search(people: list[str]):
    search_name = input("Who are you looking for? ").lower()
    results = []
    
    for person in people:
        if search_name in person["name"].lower():
            results.append(person)
        else:
            print("No person has been found. ")
            
    display_people(results)

print("Welcome to the contact management system")
print()

with open("contacts.json","r") as json_file:
    people = json.load(json_file)["contacts"]
    
while True:
    print(f"Contact list size: {len(people)}")
    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ")
    if command == "add":
        person = add_person()
        people.append(person)
        print("Person has been added. ")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command")    
    

with open("contacts.json","w") as json_file:
    people = json.dump({"contacts": people}, json_file)
        