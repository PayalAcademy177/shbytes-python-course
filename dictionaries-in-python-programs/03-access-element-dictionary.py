shbytes = {"c1": "Python", "c2": "AWS", "c3": "Azure", "c4": "Java"}

# access element using key
print("access element using key")
print(shbytes)
print("value at key c2 - ", shbytes["c2"])
# print("value at key c5 - ", shbytes["c5"])

print("\n---------------------------------------------------\n")

# access element using get method with key
print("access element using get method with key")
print(shbytes)
print("value at key c1 - ", shbytes.get("c1"))
print("value at key c5 - ", shbytes.get("c5"))

print("\n---------------------------------------------------\n")	

# get all keys of dictionary using key() method
print("get all keys of dictionary using key() method")
print(shbytes)
print("All keys in dictionary - ", shbytes.keys())
print(type(shbytes.keys()))

print("\n---------------------------------------------------\n")

# get all values of dictionary using values() method
print("get all values of dictionary using values() method")
print(shbytes)
print("All values in dictionary - ", shbytes.values())
print(type(shbytes.values()))

print("\n---------------------------------------------------\n")

# get all items of dictionary using items() method
print("get all items of dictionary using items() method")
print(shbytes)
print("All items in dictionary - ", shbytes.items())
print(type(shbytes.items()))


# Nested dictionary
print("Access items in nested dictionary")
courses = {
    "CS": {"topics": ["Algorithms", "Data Structures", "Programming Basics"]},
    "MATH": {"topics": ["Integrals", "Series", "Differential Equations"]},
    "ENG": {"topics": ["Poetry", "Prose", "Drama"]}
}
print(courses)
print("Math topics in dictionary - ", courses["MATH"]["topics"])

print("\n---------------------------------------------------\n")

# check for a key in dictionary
print("check for a key in dictionary")
print(shbytes)
if "c3" in shbytes:
    print("c3 key is in the dictionary")
if "c5" not in shbytes:
    print("c5 key is not in the dictionary")

print("\n---------------------------------------------------\n")

# access elements in nested dictionary
print("access elements in nested dictionary")
nested_dict = {"courses": {"c1": "Python", "c2": "AWS"}}
print(nested_dict)
print(nested_dict["courses"]["c1"])

print("\n---------------------------------------------------\n")

shbytes = {"c1": "Python", "c2": "Java"}

for key in shbytes.keys():
    print(f"{key}",)

for value in shbytes.values():
    print(f"{value} ")

for key, value in shbytes.items():
    print(f"{key}: {value}")
