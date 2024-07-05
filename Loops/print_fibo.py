# print fibonacci serise

n = int(input("Enter a number: "))

a = 0
b = 1
c = 0

print("Fibonacci serise: {} {}".format(a, b), end="")
# using for loop
for i in range(1, n - 2):
    c = a + b
    print("{},".format(c), end="")
    a = b
    b = c
# using while loop
i = 1
while i <= n - 2:
    c = a + b
    print(" {}".format(c), end="")
    a = b
    b = c
    i += 1
