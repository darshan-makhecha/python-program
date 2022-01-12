list = [89, 56, 90, 34, 89, 12]
print("Before process Data",list)
# Insert data in the 2nd position
list.insert(2, 23)

print("The list elements are using insert()")

print("list is : ",list)
list.append("Toshiba")


# Remove an item

list.remove(89)
list.remove(12)
print("========")
print("the slice  is :")
print(list[2])

# Print the list after delete
print("Before delete List",list)
print("List after delete")

list.clear()

print(list)

print("======")
print("the list is clear now")
list.clear()
