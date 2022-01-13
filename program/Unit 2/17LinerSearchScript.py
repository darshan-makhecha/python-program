lst = [2,5,3,1,7]
num = 6
for index,value in enumerate(lst):
    if num==value:
        print(f"{value} found at position {index+1}")
else:
    print("Value not found ")
        
