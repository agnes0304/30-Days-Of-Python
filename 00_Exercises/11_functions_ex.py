# Exercise_01
from cmath import sqrt

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1 : int, n2 : int):
    total = n1 + n2
    return total

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r : int):
    area = 3.14*r*r
    return area

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*n: int):
    total = 0
    for i in n:
        total += i
    return total

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F.
def celsius2fahrenheit(c:int):
    f = (c * (9/5)) + 32
    return f

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(m : int):
    season = str()
    if 3 <= m <= 5:
        season = 'Spring'
    elif 6 <= m <= 8:
        season = 'Summer'
    elif 9 <= m <= 11:
        season = 'Autumn'
    else:
        season = 'Winter'
    return season

# Write a function called calculate_slope which return the slope of a linear equation
def cal_slope(x1, y1, x2, y2):
    slope = abs(y2-y1) / abs(x2-x1)
    return slope

# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation.
def solve_quadratic_eqn(a, b, c):
    x1 = (-b + sqrt((b*b)-(4*a*c))) / 2*a
    x2 = (-b - sqrt((b*b)-(4*a*c))) / 2*a
    return x1, x2

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(l : list):
    for i in l:
        print(i)

# retry
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# def reverse_list(l: list):
#     for i in range(len(l)//2):
#         pass
# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list(["A", "B", "C"]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l: list):
    new_list = list()
    for item in l:
        new_list.append(item.upper())
    return new_list

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(l:list, item):
    l.append(item)
    return l          

# retry
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# def remove_item(l:list, item):
#     for i in len(l):
#         if l[i] == item:
#             l.remove(item)
#             break
#     return l
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num: int):
    total = 0
    for i in range(num+1):
        total += i
    return total

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    total = 0
    for i in range(num+1):
        if i % 2 != 0:
            total += i
    return total

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    total = 0
    for i in range(num+1):
        if i % 2 == 0:
            total += i
    return total


# Exercise_02

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num : int):
    even = 0
    odd = 0
    for i in range(num+1):
        if i % 2 == 0:
            even += 1
        else: 
            odd += 1
    return even, odd

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


# Exercsie_03

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    for i in range(2,num-1):
        if num % i != 0:
            return f'{num} is prime number.'
        else: 
            return f'{num} is not prime number.'


# 계속 unique만 나옴
# Write a functions which checks if all items are unique in the list.
def check_unique(l : list):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)-i):
            if l[i] != l[j+1]:
                return 'unique'
            else: 
                return 'not unique'


# Write a function which checks if all the items of the list are of the same data type.


# Write a function which check if provided variable is a valid python variable
