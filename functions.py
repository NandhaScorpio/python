def add():
    a = int(input("Enter num1 for adding : "))
    b = int(input("Enter num2 for adding : "))
    c = a+b
    print(c)

def sub():
    a = int(input("Enter num1 for subtraction : "))
    b = int(input("Enter num2 for subtraction : "))
    c = a-b
    print(c)

def multi():
    a = int(input("Enter num1 for multiplication : "))
    b = int(input("Enter num2 for multiplication : "))
    c = a*b
    print(c)

    
def div():
    a = int(input("Enter num1 for division : "))
    b = int(input("Enter num2 for division : "))
    c = a/b
    print(c)

userinput = input("Enter Operation : ") 

if(userinput == "add" or userinput == "Add"):
    add()
elif(userinput == "subtraction" or userinput == "Subtraction") :
    sub()
elif(userinput == "multiplication" or userinput == "Multiplication"):
    multi()
elif(userinput == "division" or userinput == "Division") :
    div()
else :
    print("Invalid Operation")

