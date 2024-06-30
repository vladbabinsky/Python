import random

chuslo = random.randint(0, 101)
UserInput = 0
attempts = 0


while UserInput != chuslo:
    UserInput = int(input('Вгадайте число (1-100): '))
    if UserInput > chuslo:
        attempts += 1
        print('Рандомне число менше\n')
    elif UserInput < chuslo:
        attempts += 1
        print('Рандомне число більше\n')

print('Ви вгадали!')
print('к-сть спроб :', attempts)