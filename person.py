class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person(name="Aron PLP", age=30, gender="male")

# Call the introduce method to display the person's information
person1.introduce()
