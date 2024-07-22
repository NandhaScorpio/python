class a():
    def __init__(self):
        print("A")
        
    def display(self):
        print("You're in class a")

class b():
    def __init__(self):
        super().__init__()
        print("B")
        
    def display(self):
        print("You're in class b")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("C")
        
    def display(self):
        print("You're in class c")

ob1= c()

