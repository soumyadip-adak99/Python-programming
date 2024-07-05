# prit factorial of a number
# using for loop
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial of {} is: {}".format(n, fact), end="")

# using while loop
i = 1
while i <= n:
    fact *= i
    i += 1

print("Factorial of {} is: {}".format(n, fact), end="")
