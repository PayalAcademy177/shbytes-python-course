#Concatenate using '+' operator
print("Concatenate using '+' operator")
x = ["Python", "Java", "AWS", "Azure"]
y = [10,20,30]
z = x + y
print("x - ", x)
print("y - ", y)
print("z - ", z)

print("\n---------------------------------------------------\n")

#Concatenate using operator plugin
print("Concatenate using operator plugin")
import operator
a = [5,6,8]
b = ["C", "C++", "Java", "Python"]
c = operator.add(a,b)
print("a - ", a)
print("b - ", b)
print("c - ", c)

print("\n---------------------------------------------------\n")

#Concatenate using itertools.chain()
print("Concatenate using itertools.chain()")
import itertools 
x = ["Python", "Java", "AWS", "Azure"]
y = [10,20,30]
z = list(itertools.chain(x, y))
print("x - ", x)
print("y - ", y)
print("z - ", z)

print("\n---------------------------------------------------\n")

# Concatenate using extend(() method
print("Concatenate using extend(() method")
x = ["Python", "NumPy", "Pandas", "Scikit-learn"]
y = [40, 50, 60]
print("x - ", x)
print("y - ", y)
y.extend(x)
print("y - ", y)

print("\n---------------------------------------------------\n")

# unpacking - (*k, *l) - using asterisk*
print("unpacking - [*k, *l] - using asterisk*")
k = [55,60,89]
l = ["AWS", "Azure", "C++", "Java"]
m = [*k , *l]
print("k - ", k)
print("l - ", l)
print("m - ", m)
