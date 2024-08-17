shbytes_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')

# creating a new tuple using condition
temp_list = []                   # Defined a new empty list
for element in shbytes_tuple:
  if "z" in element:                      # checking for condition
    temp_list.append(element)      # condition passed elements added to new list

new_shbytes_tuple = tuple(temp_list)    # new tuple is created from list
print(new_shbytes_tuple)                   # print elements in new filtered tuple

print("\n........................................")

# comprehension syntax =>
# new_shbytes_tuple = tuple(expression for item in iterable if condition == True)
# creating a new tuple using tuple comprehension without if condition
new_shbytes_tuple_4 = tuple(element for element in shbytes_tuple)
print(new_shbytes_tuple_4)

print("\n........................................")

# creating a new tuple using tuple comprehension with if-in condition
print("creating a new tuple using tuple comprehension with if-in condition")
new_shbytes_tuple_2 = tuple(element for element in shbytes_tuple if "z" in element)
print(new_shbytes_tuple_2)

# creating a new tuple using tuple comprehension with if-not condition
print("creating a new tuple using tuple comprehension with if-not condition")
new_shbytes_tuple_3 = tuple(element for element in shbytes_tuple if element != "Java")
print(new_shbytes_tuple_3)

# creating a new tuple using tuple comprehension and range function
print("creating a new tuple using tuple comprehension and range function")
new_shbytes_tuple_5 = tuple(element for element in range(10) if element > 3)
print(new_shbytes_tuple_5)