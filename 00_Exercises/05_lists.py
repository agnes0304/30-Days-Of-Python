empty_list = list() 
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']                     
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list
fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] 
print(first_fruit)      
second_fruit = fruits[1]
print(second_fruit)     
last_fruit = fruits[3]
print(last_fruit) 
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       
print(second_last)      

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] 
# this is also give the same result as the above
all_fruits = fruits[0:] 
orange_and_mango = fruits[1:3] 
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] 
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] 
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       
fruits[1] = 'apple'
print(fruits)       
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  
does_exist = 'lime' in fruits
print(does_exist)  


### LIST METHOD
# append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           
fruits.append('lime')   
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') 
print(fruits)           
fruits.insert(3, 'lime') 
print(fruits)

# remove : 항목 직접 제거
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  
fruits.remove('lemon')
print(fruits)  

# pop : 인덱스로 항목 제거 가능
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)   
# 인덱스를 주면 해당 항목 remove
fruits.pop(0)     
print(fruits)

# del : 인덱스로 항목 제거 가능
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       
del fruits[1]     
print(fruits)           

# clear : 리스트 비우기
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)   

# copying a lits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)    

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count : 리스트 내 개수 반환
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           

# index : 인덱스 값 반환
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))       # 가장 처음 나오는 24의 인덱스 값 반환

# reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()                 # 그냥 sort는 오름차순
print(ages) 
ages.sort(reverse=True)     # reverse True 설정 시 가장 큰 값부터 : 내림차순