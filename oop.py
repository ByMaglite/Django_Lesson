import os 
os.system("cls" if os.name == "nt" else "clear")

def printtype(data):
    for i in data:
        print(i, type(i))

test =[123, "Barry", [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x,{
    "name": "henry", "age": 38
}]

# printtype(test)

# Definig Classes

# class Person:
#     name = "Barry"
#     age = 44

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)


# Person.job = "teacher"

# print(person1.job)
# print(person2.job)

# #  Class Attributes ve instance attributes


# person1.name = "Henry"
# Person.name = "Rafe"

# print(person1.name)
# print(person2.name)

# Self Keyword

class Person:
    name = "Barry"
    age = 44

    def test(self):
        print("test")

    def get_details(self):
        print("name: ", self.name, "age", self.age, "location :" , self.location )

    def set_details(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

person1 = Person()
person1.test()
Person.test(person1)
person1.set_details("Henry", 37, "Ankara")
person1.get_details()