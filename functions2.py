

def add(a,b):
    sum = a+b
    return sum

def ans(n1,n2,n3):
    sumofab = add(n1,n2)
    ans = sumofab * n3
    return ans

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

answer = ans(a,b,c)


print(answer)

