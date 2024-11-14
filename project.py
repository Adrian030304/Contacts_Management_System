
people = []



for i in range(3):
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name":name,
        "age":age,
        "email":email
    }
    people.append(person)