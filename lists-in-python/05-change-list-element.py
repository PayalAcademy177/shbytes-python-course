
shbytes_list = ['Python', 'AWS', 'Java', 'Azure']

# change list values
print(shbytes_list)
shbytes_list[2] = 'Machine Learning'
print(shbytes_list)

print("\n---------------------------------------------------\n")

# change mutable elements in list
print("change mutable elements in list")
nested_list = ['Python', 'AWS', 'Azure', [1, 2, 3]]
print("original nested list", nested_list)
nested_list[3][2] = 4
print("changed mixed list", nested_list)
