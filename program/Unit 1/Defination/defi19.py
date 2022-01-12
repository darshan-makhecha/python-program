list1 = [-1,12,31,-4,-56,36,71,-28,9]

positive=0
negative= 0
num = 0


while(num < len(list1)):
    if list1[num] >  0:
        positive += 1
    else:
        negative += 1

    num += 1

print("Positive numbers in the list: ", positive)
print("Negative numbers in the list: ", negative)
