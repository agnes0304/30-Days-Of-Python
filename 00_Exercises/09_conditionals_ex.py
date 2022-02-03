# Exercises

# 09.01
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 
# Output:
    # Enter your age: 30
    # You are old enough to learn to drive.
# Output:
    # Enter your age: 15
    # You need 3 more years to learn to drive.

a = input("Enter your age: ")
if int(a) >= 18 :
    print('You are old enough to dirve')
else:
    print('you need ', 18-a, 'more years to learn to drive')


# 09.02
# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
# Output:
    # Enter your age: 30
    # You are 5 years older than me.

a = input('Enter your age: ')
my_age = 26
if int(a) > my_age:
    print('you are ', a - my_age, ' years older than me.')
elif int(a) == my_age:
    print('Same!')
else: 
    print('you are yonger than me.')


# 09.03
# Get two numbers from the user using input prompt. 
# If a is greater than b return 'a is greater than b', if a is less b return 'a is smaller than b', else 'a is equal to b'. 
# Output:
    # Enter number one: 4
    # Enter number two: 3
    # 4 is greater than 3

a = input('enter the number what you want:')
b = input('enter the number what you want:')
if int(a)>int(b):
    print(a,' is bigger than ', b)
elif int(a)<int(b):
    print(a, 'is smaller than ', b)
else: 
    print(a, b, 'are same')


# 09.04
# Write a code which gives grade to students according to theirs scores:
    # 90-100, A
    # 70-89, B
    # 60-69, C
    # 50-59, D
    # 0-49, F

s = input('enter the grade:')
def score2grade():
    if 90 <= int(s) <= 100:
        print('A')
    elif 70 <= int(s) <= 89:
        print('B')
    elif 60 <= int(s) <= 69:
        print('C')
    elif 50 <= int(s) <= 59:
        print('D')
    else:
        print('F')

score2grade()

# 09.05
# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
f = input('enter the fruit')
if f in fruits:
    print('That fruit already exist in the list')
else: 
    fruits.append(f)
    print(fruits)

# 09.06
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Jiwoo',
    'last_name': 'Choi',
    'age': 26,
    'gender': 'f',
    'country': 'Korea',
    'favorite' : ['swmming', 'purple', 'history', 'ocean', 'walking'],
    'is_married': False,
    }

# Check if the person dictionary has favorite key, if so print out the middle favorite in the favorite list.
if person.get('favorite'):
    mid = person['favorite'][len(person['favorite'])//2]
    print(mid)

# If the person is not married and if she lives in Korea, print the information in the following format:
    # Jiwoo Choi lives in Korea. She is not married.
if person['is_married'] == False and person['gender'] == 'f' and person['country'] == 'Korea':
    print(person['first_name'], ' lives in ', person['country'], '. She is not married')