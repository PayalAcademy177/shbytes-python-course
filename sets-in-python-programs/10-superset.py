
# using issuperset() method
print("using issuperset() method")
set_1 = {10, 20, 30, 70, 80, 90}
set_2 = {70, 80, 90}
superset_set12 = set_1.issuperset(set_2)
superset_set21 = set_2.issuperset(set_1)
print(set_1)
print(set_2)
print(superset_set12)
print(superset_set21)

print("\n---------------------------------------------------\n")

# using issuperset() method - with empty set
print("using issuperset() method - with empty set")
set_1 = set()
set_2 = set()
superset_set12 = set_1.issuperset(set_2)
superset_set21 = set_2.issuperset(set_1)
print(set_1)
print(set_2)
print(superset_set12)
print(superset_set21)

print("\n---------------------------------------------------\n")

# using superset (>=) operator
print("using superset (>=) operator")
set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 70, 80, 90}
superset_set12 = set_1 >= set_2
superset_set21 = set_2 >= set_1
print(set_1)
print(set_2)
print(superset_set12)
print(superset_set21)

print("\n---------------------------------------------------\n")

# using strict superset (>) operator
print("using strict superset (>) operator")
set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 70, 80, 90}
superset_set12 = set_1 > set_2
superset_set21 = set_2 > set_1
print(set_1)
print(set_2)
print(superset_set12)
print(superset_set21)

print("\n---------------------------------------------------\n")

def custom_issuperset(set_1, set_2):
    # Iterate through elements of set_2
    for element in set_2:
        # Check if any element of set_2 not in set_1
        if element not in set_1:
            return False
    return True

set_1 = {10, 20, 30}
set_2 = {10, 20, 30, 40, 50, 60}
set_3 = set()
set_4 = set()
print(custom_issuperset(set_1, set_2))  # Output: False
print(custom_issuperset(set_2, set_1))  # Output: True
print(custom_issuperset(set_3, set_4))  # Output: True