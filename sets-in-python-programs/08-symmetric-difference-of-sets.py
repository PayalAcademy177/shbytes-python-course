
# Syntax:  A.symmetric_difference_update(B)
# Parameters:
# The symmetric_difference takes a single “iterable” as an argument. Iterable should contain hashable object.
# Returns:
# This method returns None (which indicates absence of a return value). It only updates the set calling symmetric_difference_update() with the symmetric difference of sets.

# using symmetric_difference_update() method
print("symmetric_difference_update() method")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'PHP','UI','MongoDB','Java','Azure'}
difference_set12 = set_1.symmetric_difference_update(set_2)
print(set_1)
print(set_2)
print(difference_set12)

print("\n---------------------------------------------------\n")

# using symmetric_difference() method
print("symmetric_difference() method")
set_1 = {'Python','AWS','ML','Java','Azure'}
set_2 = {'PHP','UI','MongoDB','Java','Azure'}
difference_set12 = set_1.symmetric_difference(set_2)
difference_set21 = set_2.symmetric_difference(set_1)
print(set_1)
print(set_2)
print(difference_set12)
print(difference_set21)
