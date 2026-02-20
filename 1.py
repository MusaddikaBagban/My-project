import os
p=os.getcwd()
print(p)
if not os.path.exists('TempDir'):
    os.mkdir('TempDir')

user ="Mac"
age = 20
amount = 100.12
print('ab',end='')
print('12',end='')
print(f'welcome {user}, you are {age}, years old, your balance is ${amount:1.4d}')

































































