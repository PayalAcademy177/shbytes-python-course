
# join of sets - using union() method - remove duplicates
print("join of sets - using union() method - remove duplicates")
course_set_1 = {'Python','AWS','Java','Azure','ML'}
course_set_2 = {'Python', 'NumPy', 'Pandas', 'Matplotlib'}
courses = course_set_1.union(course_set_2)
print(course_set_1)
print(course_set_2)
print("course_set_1 U course_set_2 - ", courses)

print("\n---------------------------------------------------\n")

# using union() method with three sets
print("join of sets - using union() method with three sets")
number_set_1 = {10, 20, 30, 40}
number_set_2 = {30, 40, 50, 60}
number_set_3 = {60, 70, 80, 90}
number_union_1 = number_set_1.union(number_set_2).union(number_set_3)
print("number_set_1 U number_set_2 U number_set_3 - ", number_union_1)

number_union_2 = number_set_1.union(number_set_2, number_set_3)
print("number_set_1 U number_set_2 U number_set_3 - ", number_union_2)

print("\n---------------------------------------------------\n")

# union using | operator
print("join of sets - union using | operator")
number_set_1 = {10, 20, 30, 40}
number_set_2 = {30, 40, 50, 60}
number_set_3 = {60, 70, 80, 90}
number_union_1 = number_set_1 | number_set_2
print("number_set_1 U number_set_2 - ", number_union_1)

number_union_2 = number_set_1 | number_set_2 | number_set_3
print("number_set_1 U number_set_2 U number_set_3 - ", number_union_2)