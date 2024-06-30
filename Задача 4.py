list = [0, 0, 1, 4, 4, -6, -2, -6, 7]

last_negative_index = -1

for index, number in enumerate(list):
    if number < 0:
        last_number = number
        last_negative_index = index

print(f"Останній від'ємний елемент: {last_number}, індекс: {last_negative_index}")

