n1 = 5
n2 = 10

while n2 != 0:
    temp = n2
    n2 = n1 % n2
    n1 = temp
    
print("GCD:",n1)