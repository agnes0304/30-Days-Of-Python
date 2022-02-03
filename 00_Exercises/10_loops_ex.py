# Exercises
# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

count =0
while count < 10:
    print(count)
    count += 1
print(count)

# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
    #
    ##
    ###
    ####
    #####
    ######
    #######

for i in range(7):
    print('#'*(i+1))

# Use nested loops to create the following:
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #


# Print the following pattern:
    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100

for i in range(11):
    print(i, ' x ', i, ' = ', i*i)

# Iterate through the list, 
test = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
for i in range(len(test)):
    print(test[i])


# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101, 2):
    print(i)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    # The sum of all numbers is 5050.
total = 0
for i in range(101):
    total += i
print(total)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    # The sum of all evens is 2550. And the sum of all odds is 2500.
even_total = 0
for i in range(0, 101, 2):
    even_total += i
print(even_total)

odd_total = 0
for i in range(1, 101, 2):
    odd_total += i
print(odd_total)

# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.

# This is a fruit list, 
test = ['banana', 'orange', 'mango', 'lemon'] 
# reverse the order using loop.
# 3>0, 2>1, 1>2, 0>3
for i in range(len(test)//2):
    temp = test[i]
    test[i] = test[3-i]
    test[3-i] = temp
print(test)

# Go to the data folder and use the countries_data.py file.
    # What are the total number of languages in the data
    # Find the ten most spoken languages from the data
    # Find the 10 most populated countries in the world