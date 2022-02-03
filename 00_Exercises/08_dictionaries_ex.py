# Exercises

# Create an empty dictionary called dog
from turtle import st


dog = dict()

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'A'
dog['color'] = 'B'
dog['breed'] = 'C'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country and city as keys for the dictionary
student = {
    'first_name': 'Jiwoo',
    'last_name': 'Choi',
    'gender': 'f',
    'age': 26,
    'is_married': False,
    'skills': ['python'],
    'country': 'Korea',
    'city': 'Yongin',
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
st = student.items()
print(st)

# Delete one of the items in the dictionary
student.popitem()
print(student)

# Delete one of the dictionaries
del student