
def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name":name,
        "age":age,
        "email":email
    }
    return person

def delete_contact(people):
    for i, person in enumerate(people):
        print(i + 1, + "-", person["name"], "|", person["age"], "|", person["email"])

print("Welcome to the contact management system")
print()
command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ")
people = []
while True:
    if command == "add":
        person = add_person()
        people.append(person)
        print("Person has been added. ")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("Invalid command")    
    
print(people)