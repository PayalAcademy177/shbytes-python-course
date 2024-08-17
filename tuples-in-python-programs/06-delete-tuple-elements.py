
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure', 'Machine Learning')

# remove elements from tuple - using remove function
print("remove elements from tuple - using remove function")
print(shbytes_tuple)
# shbytes_tuple.remove('Java')
try:
	shbytes_tuple.remove('Java')
except AttributeError as err:
	print("error", err)
	print(shbytes_tuple)

print("\n---------------------------------------------------\n")

# remove elements from tuple - by converting it to list
print("remove elements from tuple - by converting it to list")
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
temp_list.remove("Java")
new_tuple = tuple(temp_list)
print(new_tuple)

print("\n---------------------------------------------------\n")

# remove in mutable elements in tuple
print("remove in mutable elements in tuple")
nested_tuple = ('Python', 'AWS', 'Azure', [1, 2, 3])
print("original nested tuple", nested_tuple)
nested_tuple[3].remove(2)
print("changed mixed tuple", nested_tuple)

print("\n---------------------------------------------------\n")

# Error - Case-sensitive element not in tuple
shbytes_tuple = ('Python', 'AWS', 'JAVA', 'Azure', 'Machine Learning')
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
temp_list.remove("java")
new_tuple = tuple(temp_list)


# Error - element not in tuple
# shbytes_tuple = ('Python', 'AWS', 'JAVA', 'Azure', 'Machine Learning')
# print(shbytes_tuple)
# temp_list = list(shbytes_tuple)
# temp_list.remove("GoLang")
# new_tuple = tuple(temp_list)

print("\n---------------------------------------------------\n")

del new_tuple
print(new_tuple) 	#raise an error, new_tuple no longer exists
