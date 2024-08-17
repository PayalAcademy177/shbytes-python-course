# tuple.index(element, start, end)
# element - the element to be searched
# start (optional) - start searching from this index
# end (optional) - search the element up to this index

shbytes_tuple = ("DataScience", "Azure", "AWS", "Python", 14, 15, 16)

# index of an element in tuple
print(shbytes_tuple)
y = shbytes_tuple.index("Python")
print(y)
y = shbytes_tuple.index(15)
print(y)

print("\n---------------------------------------------------\n")

# index of an element, start search from given index in tuple
print(shbytes_tuple)
y = shbytes_tuple.index("AWS", 1)               # Use index(element, start) method
print(y)

print("\n---------------------------------------------------\n")

# index of an element, start search from given index and search upto end index in tuple
print(shbytes_tuple)
y = shbytes_tuple.index("AWS", 1, 3)             # Use index(element, start, end) method
print(y)
y = shbytes_tuple.index(14, 1, 5)
print(y)

print("\n---------------------------------------------------\n")

# index of an element, which is not present in tuple
# print(shbytes_tuple)
# y = shbytes_tuple.index("Java")                 # Use index() method
# print(y)

# Error - element not present within start and end index

shbytes_tuple = ("DataScience", "Azure", "AWS", "Python", 14, 15, 16)
print(shbytes_tuple)
y = shbytes_tuple.index(14, 1, 3)
print(y)