import random

def main():
    random_numbers = []
    for i in range(10):
        random_numbers.append(random.randint(0, 100))

    max_number = random_numbers[0]
    min_number = random_numbers[0]

    for num in random_numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num

    print("Згенерований список випадкових чисел:", random_numbers)
    print("Максимальне число в списку:", max_number)
    print("Мінімальне число в списку:", min_number)

main()
