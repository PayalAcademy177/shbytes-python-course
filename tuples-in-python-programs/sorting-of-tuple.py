# sorting of alphanumeric tuple
alphanumeric_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')
print(alphanumeric_tuple)
temp_list = list(alphanumeric_tuple)
temp_list.sort()
alphanumeric_tuple = tuple(temp_list)
print(alphanumeric_tuple)

# sorting of numeric tuple
numeric_tuple = (23,45,78,13, 34, 89, 67)
print(numeric_tuple)
temp_list = list(numeric_tuple)
temp_list.sort()
numeric_tuple = tuple(temp_list)
print(numeric_tuple)

# sorting of alphanumeric tuple in descending order
alphanumeric_tuple = ('Python', 'AWS', 'Java', 'Azure', 'DataScience')
print(alphanumeric_tuple)
temp_list = list(alphanumeric_tuple)
temp_list.sort(reverse = True)
alphanumeric_tuple = tuple(temp_list)
print(alphanumeric_tuple)

# sorting of numeric tuple in descending order
numeric_tuple = (23,45,78,13, 34, 89, 67)
print(numeric_tuple)
temp_list = list(numeric_tuple)
temp_list.sort(reverse = True)
numeric_tuple = tuple(temp_list)
print(numeric_tuple)