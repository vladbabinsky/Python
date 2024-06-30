list = [-6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]

for index, number in enumerate(list):
    if number > 0:
        print(f"Перший додатній елемент: {number}, індекс: {index}")
        break
