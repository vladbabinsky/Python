import random

chuslo = random.randint(1, 100)
UserInput = 0

while UserInput != chuslo:
    UserInput = int(input('Вгадайте число (1-100): '))
    if UserInput > chuslo:
        print('Рандомне число менше\n')
    elif UserInput < chuslo:
        print('Рандомне число більше\n')

print('Ви вгадали!')
