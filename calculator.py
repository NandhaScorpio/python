class calculator :
    def add(self,a,b):
        c = a+b
        print(c)
    def sub(self,a,b):
        c = a-b
        print(c)
    def mul(self,a,b):
        c = a*b
        print(c)
    def div(self,a,b):
        c = a/b
        print(c)

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

calc = calculator()
calc.div(num1,num2)
