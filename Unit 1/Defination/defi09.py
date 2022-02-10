Number = int(input("Enter the Number to Check Pronic Number = "))

flag = 0

for i in range(Number + 1):
    if Number == i * (i + 1):
        flag = 1
        break

if flag == 1:
    print("\n%d is a Pronic Number." %Number)
else:
    print("%d is Not a Pronic Number." %Number)
