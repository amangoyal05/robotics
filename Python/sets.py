# Kind of like a list but no duplicates. 
# Sets are really useful for solving a certain set of problems such as Intersection, Difference
s1 = set([1, 2, 3, 4, 5])
print(s1)

s1 = {1, 2, 3, 4, 5, 1, 2, 3, 4}
print(s1)

# To create empty set
s2 = set()
print(s2)
# s2 = {}               This will create an empty dictionary

# Adding a value to a set
s1.add(6)
print(s1)

# Adding multiple values to a set
s1.update([7, 8])
print(s1)

# Adding values and values in another set to a set
s2 = {7, 8, 9}
s1.update([6, 7, 8], s2)
print(s1)


# Removing values from set
s1.remove(5)
print(s1)

s1.discard(9)
print(s1)

# Difference between remove and discard - 
# Remove will throw an error (KeyError) if we remove a value that does not exist in the set
# Discard will not throw any error of such sort
# s1.remove(11)
s1.discard(11)
print(s1)

# Operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4 ,5}

s4 = s1.intersection(s2, s3)
print(s4)

s4 = s1.difference(s2, s3)
print(s4)

s4 = s2.difference(s1, s3)
print(s4)

s4 = s3.difference(s1, s2)
print(s4)

# symmetric_difference gives the different elements in both, s1 and s2. 
s4 = s1.symmetric_difference(s2)
print(s4)

# Removing duplicates from a list using sets
l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
print(l2)


employees = ['Aman', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Aman']

developers = ['Judy', 'Aman', 'Steven', 'Jane', 'April']

result = list(set(gym_members).intersection(developers))
print(result)

result = list(set(employees).difference(gym_members, developers))
print(result)

if 'Aman' in developers:
    print('Found!')

# O(n) for finding an element in list
# O(1) for finding an element in set