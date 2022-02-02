# Exercises: Level 1

# Declare a first name variable and assign a value to it
from itertools import count, product
from tarfile import FIFOTYPE
from turtle import Turtle


first_name = 'jiwoo'
# Declare a last name variable and assign a value to it
last_name = 'choi'
# Declare a full name variable and assign a value to it
full_name = 'jiwoo choi'
# Declare a country variable and assign a value to it
country = 'korea'
# Declare a city variable and assign a value to it
city = 'yongin'
# Declare an age variable and assign a value to it
age = 26
# Declare a year variable and assign a value to it
year = 2022
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = True
# Declare multiple variable on one line
school, is_graduate = 'SNU', False
print(school)
print(is_graduate)

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(is_light_on))
print(type(age))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
print(len(first_name)>len(last_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two


# The radius of a circle is 30 meters.
radius = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = radius ** 2 * 3.14
print(area_of_circle)

# Take radius as user input and calculate the area.
radius = input()
area_of_circle = int(radius) ** 2 * 3.14
print(area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
your_full_name = input()
your_country = input()
your_age = input()

user_info = {
    'name' : your_full_name, 
    'country' : your_country, 
    'age' : your_age
    }

print(user_info)