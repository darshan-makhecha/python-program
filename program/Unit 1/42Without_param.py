def print_key1(): 
 return "This is Gfg's value"
 
# initializing dictionary 
# check for function name as key 
test_dict = {"Gfg": print_key1, "is" : 5, "best" : 9}
print("The original dictionary is : " + str(test_dict)) 
 
# calling function using brackets 
res = test_dict['Gfg']() 
 
# printing result 
print("The required call result : " + str(res)) 
