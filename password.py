import random
import string

LowerCase = string.ascii_lowercase
UpperCase = string.ascii_uppercase
Digits = string.digits
punctuation = string.punctuation

char_set = ""

UserAnswer = 0

a = '(1) Малі літери\n'
b = '(2) Великі літери\n'
c = '(3) Цифри\n'
d = '(4) Спеціальні символи\n'
e = '(5) Завершити вибір та згенерувати пароль\n'

print(f'Enter password length: ')
passlength = int(input())
print(f'Choose the classes of symbols for your password:\n{a}{b}{c}{d}{e}')

while UserAnswer != 5:
    UserAnswer = int(input('Your choice: '))
    if UserAnswer == 1:
        a = ''
        char_set += LowerCase
    elif UserAnswer == 2:
        b = ''
        char_set += UpperCase
    elif UserAnswer == 3:
        c = ''
        char_set += Digits
    elif UserAnswer == 4:
        d = ''
        char_set += punctuation

    if UserAnswer != 5:
        print(f'do you want to add new characters?\n{a}{b}{c}{d}{e}')
        

print('Generated password: ', end='')
for i in range(passlength):
        print(random.choice(char_set), end='')
