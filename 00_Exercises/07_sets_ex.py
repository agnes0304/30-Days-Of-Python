# Exercises

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
test = ['A', 'B', 'C']
it_companies.update(test)
print(it_companies)

# Remove one of the companies from the set it_companies
test = it_companies.pop()
print(test)


# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))


# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B
del C

# Convert the age list to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age_set))
print(len(age))


test = 'I am a teacher and I love to inspire and teach people.' 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
test_list = test.split(' ')
test_set = set(test_list)
print(len(test_set))