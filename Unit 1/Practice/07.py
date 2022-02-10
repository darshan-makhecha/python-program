set = {"apple", "banana","cherry"}

print("Before insert value in set" , set)

set.add("mango")
set.add("stroberry")
set.add("Guavava")
print("After add items in set " , set)

print("=================")
print("Before remove data using delete()" , set)
set.remove("banana") #error aape
print("after delete an item in set" , set)

print("============")
print("Before remove data using discard() " ,set)
set.discard("Guavava")# error no aape

print("After remove an item in set ",set)
print("==========")
print("The clear() use after set is clear ")
print("Before clear() set is : ",set)
set.clear()
print("the set is clear ")
