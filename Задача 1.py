list = [1, 2, 3, 4, 5, 6, -6, -5, -4, -3, -2, -1, 132, 456, 0, 0, 1, 4, 4, -6, 2, 6, -7]

positive_count = 0
negative_count = 0

for number in list:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

print("Кількість додатних чисел:", positive_count)
print("Кількість від'ємних чисел:", negative_count)
