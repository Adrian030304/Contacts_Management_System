
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

print("Welcome to the contact management system")
print()
command = input("You can 'Add', 'Delete', or 'Search': ")
people = []
while True:
    if command == "add":
        person = add_person()
        people.append(person)
        print("Person has been added. ")
    elif command == "delete":
        pass
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("Invalid command")    
    
print(people)