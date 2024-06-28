import random
import string
a = int(input('Введіть довжину пароля: \t'))
clas = int(input('''Виберіть клас символів з якого вам згенерувати пароль : 
(1) Малі літери
(2) Великі літери
(3) Цифри
(4) Спеціальні символи \n'''))



LowerCase = string.ascii_lowercase
UpperCase = string.ascii_uppercase
Digits = string.digits
punctuation = string.punctuation

if clas == 1:
    for i in range(a):
        print(random.choice(LowerCase), end='')
elif clas == 2:
    for i in range(a):
        print(random.choice(UpperCase), end='')
elif clas == 3:
    for i in range(a):
        print(random.choice(Digits), end='')
elif clas == 4:
    for i in range(a):
        print(random.choice(punctuation), end='')