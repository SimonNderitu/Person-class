class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class
person1 = Person("Simon Nderitu", 25, "Male")

# Call the introduce method
person1.introduce()
print(person1.name)