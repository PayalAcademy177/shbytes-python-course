
shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure')

# change tuple values - TypeError
print("change tuple values - TypeError")
print(shbytes_tuple)
# shbytes_tuple[2] = 'Machine Learning'
try:
	shbytes_tuple[2] = 'Machine Learning'
except TypeError as err:
	print("error", err)
	print(shbytes_tuple)

print("\n---------------------------------------------------\n")

# change tuple values - by converting it to list
print("change tuple values - by converting it to list")
print(shbytes_tuple)
temp_list = list(shbytes_tuple)
temp_list[2] = 'Machine Learning'
new_tuple = tuple(temp_list)
print(new_tuple)

print("\n---------------------------------------------------\n")

# change mutable elements in tuple
print("change mutable elements in tuple")
nested_tuple = ('Python', 'AWS', 'Azure', [1, 2, 3])
print("original nested tuple", nested_tuple)
nested_tuple[3][2] = 4
print("changed mixed tuple", nested_tuple)
