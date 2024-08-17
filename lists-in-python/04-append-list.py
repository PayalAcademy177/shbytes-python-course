# append element in the list using append method
sybytes_list = ['Python', 'AWS', 'Java', 'Azure']
print(sybytes_list)
sybytes_list.append("Machine Learning")
print(sybytes_list)

print("\n---------------------------------------------------\n")

# append element in nested element of a list
print("append in mutable elements in list")
nested_list = ['Python', 'AWS', 'Azure', [1, 2, 3]]
print("original nested list", nested_list)
nested_list[3].append(4)							# access index 3 element in list and append 4 in that list element
print("changed mixed list", nested_list)
