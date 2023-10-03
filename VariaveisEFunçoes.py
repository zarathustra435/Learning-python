#Variaveis em Python
first_name = 'Bryan'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 67
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

#Fazendo print de todos os valores armazenados nas variaveis
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declarando multiplas variaveis
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Usando a função input
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#Checando o tipo de dados
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))   # str
print(type(first_name))   # str
print(type(10))   # int
print(type(3.14))   # float
print(type(1 + 1j))   # complex
print(type(True))   # bool
print(type([1, 2, 3, 4]))   # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))   # tuple
print(type(zip([1,2],[3,4])))   # set

#Convertendo o tipo de dados
