# find the greates number

a = int(input("Enter number of A: "))
b = int(input("Enter number of B: "))
c = int(input("Enter number of C: "))

if a >= b and a >= c:
    print("A is a greatest number.")
elif b >= c:
    print("B is a greatest number.")
else:
    print("C is a greatest number.")
