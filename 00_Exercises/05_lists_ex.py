# Exercises
# Declare an empty list
list = []

# Declare a list with more than 5 items
list = [1,2,3,4,5]

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
print(list[0])
print(list[len(list)//2])
print(list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
list = ['jiwoo', 26, 168, 'solo', 'yongin']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'LG'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('IT company')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'IT company')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
companies = '#; '.join(it_companies)
print(companies)

# Check if a certain company exists in the it_companies list.
print('samsung' in it_companies)
print('Apple' in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
l = it_companies[3:]

# Slice out the last 3 companies from the list
l = it_companies[:-3]

# Slice out the middle IT company or companies from the list
l = []  
if len(it_companies) % 2 == 0:
    l = it_companies[:len(it_companies)/2] + it_companies[len(it_companies)/2+1:]
else:
    l = it_companies[:len(it_companies)//2] + it_companies[len(it_companies)//2+1:]
print(l)
 
# Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.remove(it_companies[len(it_companies)//2])
print(it_companies)

# Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
skills = front_end + back_end
print(skills)

# After joining the lists, copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.
full_stack = skills
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()   
print(ages)
maxage = max(ages)
minage = min(ages)
print(maxage, minage)

# Add the min age and the max age again to the list
ages.append(maxage)
ages.append(minage)
print(ages)


# Find the average age (sum of all items divided by their number)
total = 0
for i in range(len(ages)):
    total += ages[i]

average = total / len(ages)
print(average)

# Find the range of the ages (max minus min)
age_range = maxage - minage
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(minage - average) > abs(maxage - average))

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
test = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
front = test[:len(test)//2+1]
back = test[len(test)//2+1:]
print(front, back)

# Unpack the first three countries and the rest as scandic country
other = test[:3]
scandic = test[3:]
print(other, scandic)
