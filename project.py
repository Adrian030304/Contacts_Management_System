
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

people = []

print("Welcome to the contact management system")
print()
command = input("You can 'Add', 'Delete', or 'Search': ")

if command == "add":
    person = add_person()
    people.append(person)
elif command == "delete":
    pass
elif command == "search":
    pass
else:
    print("Invalid command")    