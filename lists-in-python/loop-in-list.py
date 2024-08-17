sybytes_list = ['Python', 'AWS', 'Java', 'Azure', 'Data Science']

# for loop with list elements
for element in sybytes_list:
    print(element)

print("\n...............................\n")

# for loop with list using index
for index in range(len(sybytes_list)):
    print(sybytes_list[index])

print("\n...............................\n")

# while loop with list using index
index = 0
while index < len(sybytes_list):
    print(sybytes_list[index])
    index += 1

print("\n...............................\n")

# loop through the list using list comprehension
[print(x) for x in sybytes_list]

print("\n...............................\n")

# creating lists in a loop
shbytes_list = ['Python']
for i in range(5):
    shbytes_list = [shbytes_list]
    print(shbytes_list)
