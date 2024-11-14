
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
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])
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
print("Welcome to the contact management system")
print()
people = []

while True:
    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ")
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