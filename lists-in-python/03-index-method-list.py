# list.index(element, start, end)
# element - the element to be searched
# start (optional) - start searching from this index
# end (optional) - search the element up to this index

shbytes_list = ["DataScience", "Azure", "AWS", "Python", 14, 15, 16]

# index of an element in list
print(shbytes_list)
y = shbytes_list.index("Python")
print(y)
y = shbytes_list.index(15)
print(y)

print("\n---------------------------------------------------\n")

# index of an element, start search from given index in list
print(shbytes_list)
y = shbytes_list.index("AWS", 1)               # Use index(element, start) method
print(y)

print("\n---------------------------------------------------\n")

# index of an element, start search from given index and search upto end index in list
print(shbytes_list)
y = shbytes_list.index("AWS", 1, 3)             # Use index(element, start, end) method
print(y)
y = shbytes_list.index(14, 1, 3)
print(y)

print("\n---------------------------------------------------\n")

# index of an element, which is not present in list
print(shbytes_list)
y = shbytes_list.index("Java")                 # Use index() method
print(y)
