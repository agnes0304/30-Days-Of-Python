# Exercise

# Declare your age as integer variable
age = 26
# Declare your height as a float variable
height = 168
# Declare a variable that store a complex number
complex_number = 1 + 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input('enter base : '))
h = float(input('enter height : '))
area_of_your_triangle = 0.5 * b * h
print('area of your triangle: ', area_of_your_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_1 = int(input('enter side1 :'))
side_2 = int(input('enter side2 :'))
side_3 = int(input('enter side3 :'))
perimeter_of_your_triangle = side_1 + side_2 + side_3
print('perimeter of your triangle: ', perimeter_of_your_triangle)


# Find the length of the text python and convert the value to float and convert it to string
print(float(len('python')))
print(str(float(len('python'))))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
n = int(input('enter the number you want to check : '))
if n % 2 == 0 : 
    print('even number')
else:
    print('odd number')


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
print(type('10')==type(10))

# Check if int(9.8) is equal to 10
print(int(9.8) == 10)


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
h = int(input('enter your working hours : '))
r = int(input('enter your rate : '))
e = h * r
print('Your weekly earning is :', e)

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125