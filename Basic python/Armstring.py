n = 158
rute = len(str(n))
copy = n
sum = 0

while (n != 0):
    digit = n % 10
    sum += digit**rute
    n = n // 10

if (sum == copy):
    print(f"{copy} is armstrong number")
else:
    print(f"{copy} is not a armstrong number")
