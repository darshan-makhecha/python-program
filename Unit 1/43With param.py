def sum_key(a, b): 
 return a + b 
 
# initializing dictionary 
# check for function name as key 
test_dict = {"Gfg": sum_key, "is" : 5, "best" : 9}
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
 
# calling function using brackets 
# params inside brackets 
res = test_dict['Gfg'](10, 34) 
 
# printing result 
print("The required call result : " + str(res))
