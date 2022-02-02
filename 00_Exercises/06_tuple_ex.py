# Create an empty tuple
T = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
boys = ('DH', 'SJ', 'CJ')
girls = ('JW', 'JW', 'JN')

# Join brothers and sisters tuples and assign it to siblings
siblings = boys + girls
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parent = ('MOM', 'DAD')
family_members = siblings + parent
print(family_members)

# Unpack siblings and parents from family_members
s = len(family_members) - len(parent)
p = len(family_members) - len(siblings)
siblings = family_members[0:s]
parent = family_members[s:]
print(siblings)
print(parent)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'pear')
vegetables = ('carrot', 'onion')
animal = ('cow', 'chicken')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
m = len(food_stuff_lt) // 2
middle_item = food_stuff_lt.pop(m)
print(food_stuff_lt)
print(middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
front = food_stuff_lt[:3]
back = food_stuff_lt[-3:]
print(front)
print(back)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)