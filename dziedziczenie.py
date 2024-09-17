

class Person:

    def __init__(self, first_name, last_name, b_year):
        self.first_name = first_name
        self.last_name = last_name
        self.b_year = b_year

    @property
    def age(self):
        return 2024 - self.b_year


class StudyMixing:
    def study(self):
        print("Student sie uczy")

class Student(Person, StudyMixing):
    def __init__(self, first_name, last_name, b_year, group):
        super().__init__(first_name, last_name, b_year)
        self.group = group
    


s = Student("A", "B", 2012, "A1")
print(s.age)

s.age = 600


s.study()

p = Person("Rafal", "K", 1980)

print(p.age())
# p.study()



class Animal:

    def __init__(self, name):
        self.name = name

    def voice(self):
        print("Nie wiadomo")


class Cat(Animal):

    def voice(self):
        print("Miau")