list=[1,2,3,45,78,1,6,2,9,6] #create list
my_list=sorted(list) #sorted list  store  in my_list
 
duplicates=[] #create empty list for duplicate value store

for i in my_list:  #use of for loop here i is var and check my_list
    
     if my_list.count(i)>1: #check  1 less than my_list
         if i not in duplicates: 
             duplicates.append(i)#here append () is Adds its argument as a single element to the end of a list. 
 
print(duplicates)
