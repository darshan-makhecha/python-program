list1 = ['abc','avd', 15, 9, 56, 17]
print("Before interchange first and last elements in a list:",list1)
length = len(list1) #check length
temp = list1[0]
list1[0] = list1[length - 1]
list1[length - 1] = temp
print("After interchange first and last elements in a list:",list1)
