class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary

class Manager(Employee):
    def __init__(self,name,salary,dept):
        self.dept = dept
        super().__init__(name,salary)

    def display(self):
        print("Name :",self.name)
        print("Salary :",self.salary)
        print("Department :",self.dept)

m1 = Manager("Nandha",100000,"FSWD")
m1.display()
