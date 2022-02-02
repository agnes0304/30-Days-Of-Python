# Single line comment
letter = 'P'                
print(letter)               
print(len(letter))          
greeting = 'Hello, World!'  
print(greeting)             
print(len(greeting))        
sentence = "I wanna complete 30 days of python challenge in 2 weeks."
print(sentence)

# Multiline String: '''~''' or """~"""
multiline_string = '''I am a student and try to enjoy coding.
Software engineering is not my major so I need to study programming in another way.
That is why I started 30 days of python, Thx.'''
print(multiline_string)

multiline_string = """I am a student and try to enjoy coding.
Software engineering is not my major so I need to study programming in another way.
That is why I started 30 days of python, Thx."""
print(multiline_string)

# String Concatenation
first_name = 'Jiwoo'
last_name = 'Choi'
space = ' '
full_name = first_name + space + last_name
print(full_name) 

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

# Slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three)
# Another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Skipping character while splitting Python strings
# 0번째부터 5번째까지, 2개에 하나 출력
language = 'Python'
pto = language[0:6:2] 
print(pto)

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')


## String Methods

# capitalize(): Converts the first character the string to Capital Letter
challenge = 'thirty days of python'
print(challenge.capitalize())

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on')) 
print(challenge.endswith('tion'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# format()	formats string into nicer output    
first_name = 'Jiwoo'
last_name = 'Choi'
job = 'student'
country = 'Korea'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) 

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.index('y')) 
print(challenge.index('th'))

# isalnum(): Checks alphanumeric(문자+숫자) character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) 

challenge = '30DaysPython'
print(challenge.isalnum()) 

challenge = 'thirty days of python'
print(challenge.isalnum()) 

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) 

# isalpha(): Checks if all characters are alphabets
challenge = 'thirty days of python'
print(challenge.isalpha()) 
num = '123'
print(num.isalpha())      

# isnumeric():Checks numeric characters
num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# isdecimal(): Checks Decimal Characters
# isdigit(): Checks Digit Characters
challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit()) 
print(challenge.isdecimal())

# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) 
# 숫자로 시작할 수 없음. 
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 

# islower():Checks if all alphabets in a string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) 
challenge = 'Thirty days of python'
print(challenge.islower()) 

# isupper(): returns if all characters are uppercase characters
challenge = 'thirty days of python'
print(challenge.isupper()) 
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) 

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) 
# 'HTML# CSS# JavaScript# React'

# strip(): 앞 뒤 character 제거
challenge = '-thirty days of python-'
print(challenge.strip('-'))

# replace(): Replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) 

# split():Splits String from Left
challenge = 'thirty days of python'
print(challenge.split()) 

# title(): 첫번째 문자, 공백 다음 문자 2대문자
challenge = 'thirty days of python'
print(challenge.title()) 
# Thirty Days Of Python

# swapcase(): 소문자2대문자, 대문자2소문자
challenge = 'thirty days of python'
print(challenge.swapcase())   
# THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  
# tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) 
challenge = '30 days of python'
print(challenge.startswith('thirty')) 