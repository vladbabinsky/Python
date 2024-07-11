import random

def start():
    user = ''
    computer = ''

    UserChoice = input('''
Введіть "player", щоб почати гру з себе
Введіть "computer", щоб почати гру з комп'ютера
''')

    if UserChoice.lower() == 'player':
        player_select = input('Зробіть вибір: "камінь", "ножиці" або "папір"\n').lower()
        computer_select = random.choice(['камінь', 'ножиці', 'папір'])
        print(f'Комп\'ютер вибрав: {computer_select}')
    elif UserChoice.lower() == 'computer':
        computer_select = random.choice(['камінь', 'ножиці', 'папір'])
        print(f'Комп\'ютер вибрав: {computer_select}')
        player_select = input('Зробіть вибір: "камінь", "ножиці" або "папір"\n').lower()
    else:
        print('Спробуйте ще раз.')
        return start()

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


    elif player_select == 'камінь' and computer_select == 'камінь':
        print('нічия')
    elif player_select == 'ножиці' and computer_select == 'ножиці':
        print('нічия')
    elif player_select == 'папір' and computer_select == 'папір':
        print('нічия')


    else:
        print('Ви програли')

start()
