
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Age']: " , dict['Age'])

print("dict['class']: ", dict['Class'])


del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print(dict)
