list1 = [1,2,3,4,5,6,7,8,9]

even =0
odd = 0
num = 0

# using while loop
while(num < len(list1)):
    if list1[num] % 2 == 0:
        even +=1
    else:
        odd +=1

    num +=1

print("Even numbers in the list: ", even)
print("Odd numbers in the list: ", odd)
