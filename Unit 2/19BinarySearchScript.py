lst = [1,3,2,4,5,6,9,8,7,10]
lst.sort()
first=0
last=len(lst)-1
mid = (first+last)//2
item = 32
found = False
while( first<=last and not found):
    mid = (first + last)//2
    if lst[mid] == item :
        print(f"found at location {mid+1}")
        found= True
    else:
        if item < lst[mid]: 
          last = mid - 1
        else:
          first = mid + 1
if found == False:
    print("Number not found")

#BubbleSort
