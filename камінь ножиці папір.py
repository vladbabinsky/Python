import random

def start():
    user = ''
    computer = ''

    UserChoice = input('''
Введіть "player", щоб почати гру з себе
Введіть "computer", щоб почати гру з комп'ютера
''')

    if UserChoice.lower() == 'player':
        while True:

            player_select = input('Зробіть вибір: "камінь", "ножиці" або "папір"\n').lower()
            if player_select == 'камінь' or player_select == 'ножиці' or player_select == 'папір':
                break
            else:
                print('Неправильний вибір. Спробуйте ще раз.')

        computer_select = random.choice(['камінь', 'ножиці', 'папір'])
        print(f"Комп'ютер вибрав: {computer_select}")

    elif UserChoice.lower() == 'computer':
        computer_select = random.choice(['камінь', 'ножиці', 'папір'])
        print(f"Комп'ютер вибрав: {computer_select}")

        while True:
            player_select = input('Зробіть вибір: "камінь", "ножиці" або "папір"\n').lower()
            if player_select == 'камінь' or player_select == 'ножиці' or player_select == 'папір':
                break
            else:
                print('Неправильний вибір. Спробуйте ще раз.')

    if computer_select == 'камінь':
        computer = 'камінь'
    elif computer_select == 'ножиці':
        computer = 'ножиці'
    elif computer_select == 'папір':
        computer = 'папір'

    if player_select == 'камінь':
        user = 'камінь'
    elif player_select == 'ножиці':
        user = 'ножиці'
    elif player_select == 'папір':
        user = 'папір'

    if player_select == 'камінь' and computer_select == 'ножиці':
        print('Ви виграли')
    elif player_select == 'ножиці' and computer_select == 'папір':
        print('Ви виграли')
    elif player_select == 'папір' and computer_select == 'камінь':
        print('Ви виграли')
    elif player_select == computer_select:
        print('Нічия')
    else:
        print('Ви програли')

start()
