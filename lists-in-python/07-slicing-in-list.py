#slicing using colon (:) operator
#list[start:end:step]

#slicing using slice method
#slice(start, end, step)

sybytes_list=[0,1,2,3,4,5,6,7,8,9,10,1]

#length of a list
print("length of a list")
print(sybytes_list, type(sybytes_list))
print("length of list", len(sybytes_list))

print("\n---------------------------------------------------\n")

#slicing range will be from index 1 to 3 (end - 1)
print("slicing range will be from index 1 to 3 (end - 1)")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[1:4])
print(sybytes_list)
print(sybytes_list[slice(1, 4)])
print(sybytes_list)

print("\n---------------------------------------------------\n")

#slicing will not throw an error, if end index is more than list limit
print("slicing will not throw an error, if end index is more than list limit")
print(sybytes_list[2:14])
print(sybytes_list[slice(2, 14)])
print(sybytes_list)

print("\n---------------------------------------------------\n")

#slicing value from index 1 to end of the list
print("slicing value from index 1 to end of the list")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[1:])                 # colon operator, end index not required
print(sybytes_list[slice(1, -1)])       # slice method, end index with negative indexing
print(sybytes_list[slice(1, 12)])       # slice method, end index with positive indexing
print(sybytes_list)

print("\n---------------------------------------------------\n")

#slicing value from index 0 to 3 of the list
print("slicing value from index 0 to 3 of the list")
print(sybytes_list[:4])
print(sybytes_list[slice(4)])
print(sybytes_list, type(sybytes_list))

print("\n---------------------------------------------------\n")

# Slicing end index - Negative indexing
print("Slicing end index - Negative indexing")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[:-1])
print(sybytes_list[slice(-1)])

print("\n---------------------------------------------------\n")

# Slicing start and end index - Negative indexing
print("Slicing start and end index - Negative indexing")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[-3:-1])
print(sybytes_list[slice(-3,-1)])

print("\n---------------------------------------------------\n")

#slicing value from index position 0 to (list limit - 1) from left
print("slicing value from index position 0 to (list limit - 1) from left")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[0:-1])
print(sybytes_list[slice(0, -1)])

print("\n---------------------------------------------------\n")

#slicing value from index position 0 to 10 from left
print("slicing value from index position 0 to 10 from left")
print(sybytes_list, type(sybytes_list))
print(sybytes_list[0:11])
print(sybytes_list[slice(0,11)])

print("\n---------------------------------------------------\n")

# Slicing left to right - Positive step
print("Slicing left to right - Positive step")
sybytes_list=[0,1,2,3,4,5,6,7,8,9,10,11]
print(sybytes_list, type(sybytes_list))
print(sybytes_list[::2])
print(sybytes_list[slice(0, -1, 2)])

print("\n---------------------------------------------------\n")

# Slicing right to left - Negative step
print("Slicing right to left - Negative step")
sybytes_list=[0,1,2,3,4,5,6,7,8,9,10,11]
print(sybytes_list, type(sybytes_list))
print(sybytes_list[::-2])
print(sybytes_list[slice(-1, 0, -2)])
