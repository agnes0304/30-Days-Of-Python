# Exercise

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
from re import U


full = 'Thrity ' + 'Days ' + 'Of ' + 'Python'
print(full)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
full = 'Coding ' + 'For ' + 'All'
print(full)
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
print(len(full))

# Change all the characters to uppercase letters using upper() method.
print(full.upper())
# Change all the characters to lowercase letters using lower() method.
print(full.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(full.capitalize())
print(full.title())
print(full.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(full[0])
print(full[1:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
full = 'Coding For All'
if full.find('Coding'):
    print('the word /"Coding/" exists')
else:
    print('no word')

# Replace the word coding in the string 'Coding For All' to Python.
full = 'Coding For All'
full.replace('Coding', 'Python')
print(full)

# Split the string 'Coding For All' using space as the separator (split()).
full.split(' ')
print(full)

test = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# split the string at the comma.
noComma = test.split(',')
print(noComma)

# What is the character at index 0 in the string Coding For All.
full = 'Coding For All'
print(full[0])

# What is the last index of the string Coding For All.
print(full[-1])

# What character is at index 10 in "Coding For All" string.
print(full[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# acronym; 머리 글자 / abbreviation; 약어

w = str(input())
def acronym():
    u_list = []
    for i in range(len(w.split(' '))):
        u_list.append(w.split(' ')[i][0].upper())

    value = str()
    for i in range(len(u_list)):
        value += u_list[i]
    
    print(value)

# acronym()


# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 
test = 'You cannot end a sentence with because because because is a conjunction'
print(test.find('because'))

# Slice out the phrase 'because because because' in the following sentence: 
test = 'You cannot end a sentence with because because because is a conjunction'
target = 'because because because'
f = test.find('because because because')
b = test.find('because because because') + len(target) - 1
result = test[:f] + test[b+1:]
print(result)

test = 'Coding For All'
# Does ''Coding For All' start with a substring Coding?
print(test.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print(test.startswith('coding'))

test = '   Coding For All   ' 
# remove the left and right trailing spaces in the given string.
print(test.strip('   '))

# Which one of the following variables return True when we use the method isidentifier():
a = ' 30DaysOfPython'
b = 'thirty_days_of_python'
print(a.isidentifier())
print(b.isidentifier())

# The following list contains the names of some of python libraries: 
lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the list with a hash with space string.
value = print("# ".join(lib))