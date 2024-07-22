class Person():
    def __init__(self,name_input):
        self.name = name_input

class Student(Person):
    def __init__(self,name,grade):
        self.std = grade
        super().__init__(name)

    def display(self):
        print("Name :",self.name)
        print("Grade :",self.std)

s1 = Student("Nandha",9)
s1.display()
