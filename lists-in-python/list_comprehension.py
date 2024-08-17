sybytes_list = ['Python', 'AWS', 'Java', 'Azure', 'DataScience']

# creating a new list using condition
new_shbytes_list = []
for element in sybytes_list:
  if "z" in element:
    new_shbytes_list.append(element)

print(new_shbytes_list)

# creating a new list using list comprehension without if condition
new_shbytes_list_4 = [element for element in sybytes_list]
print(new_shbytes_list_4)

# creating a new list using list comprehension with if condition
# comprehension syntax =>
# new_shbytes_list = [expression for item in iterable if condition == True]
print("\ncreate a new list using list comprehension and if-in condition")
new_shbytes_list_2 = [element for element in sybytes_list if "z" in element]
print(new_shbytes_list_2)

print("\ncreate a new list using list comprehension and if condition")
new_shbytes_list_3 = [element for element in sybytes_list if element != "Java"]
print(new_shbytes_list_3)

# create a new list using list comprehension and range function
print("\ncreate a new list using list comprehension and range function")
new_shbytes_list_5 = [element for element in range(10) if element > 3]
print(new_shbytes_list_5)