# print fibonacci serise

n = int(input("Input a number: "))

a, b = 0, 1
c = 0

print("Fibonacci serise: {} {}".format(a, b), end=" ")

for i in range(n - 2):
    c = a + b
    print("{}".format(c), end=" ")
    a = b
    b = c
