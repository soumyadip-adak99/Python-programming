# print a numbers 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# print a numbers 100 to 1
j = 100
while j >= 1:
    print(j)
    j -= 1

# print a the multiplication table of a number n.
i = 1
n = 3
while i <= 10:
    r = n * i
    print(n, "x", i, "=", r)
    i += 1


# Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
while index < len(number):
    print(number[index])
    index += 1

# Search for a number x in this tuple using loop : (1,4,9,16,25,36,49,64,81,100)
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36

i = 0
while i < len(tup):
    if tup[i] == x:
        print(x, "fonnd at index:", i)
    i += 1

# Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100) first find the x present in a tuple then find the x
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36

found = False
index = 0

j = 0
while j < len(tup):
    if tup[j] == x:
        found = True
        index = j
        break
    j += 1

if found:
    print(x, "found at index:", index)
else:
    print(x, "NOT FOUND")
