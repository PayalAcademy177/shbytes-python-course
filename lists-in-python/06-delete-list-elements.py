
shbytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Machine Learning', 'Java']

# remove elements from list - using remove function
print("remove elements from list - using remove function")
print(shbytes_list)
shbytes_list.remove('Java')
print(shbytes_list)

print("\n---------------------------------------------------\n")

# remove in mutable elements in list
nested_list = ['Python', 'AWS', 'Azure', [1, 2, 3]]
print("original nested list", nested_list)
nested_list[3].remove(2)
print("changed mixed list", nested_list)

print("\n---------------------------------------------------\n")

# Error - Case-sensitive element not in list
shbytes_list = ['Python', 'AWS', 'JAVA', 'Azure', 'Machine Learning']
print(shbytes_list)
shbytes_list.remove('java')
print(shbytes_list)


# Error - element not in list
shbytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Machine Learning', 'Java']
print(shbytes_list)
shbytes_list.remove('GoLang')
print(shbytes_list)

del nested_list
print(nested_list) 	#raise an error, new_list no longer exists
