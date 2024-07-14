import random

def random_list():
    random_list = []
    for i in range(10):
        random_list.append(random.randint(1, 100))
    return random_list

def find(numbers):
    
    minn = numbers[0]
    maxx = numbers[0]
    
    for num in numbers:
        if num < minn:
            minn = num
        if num > maxx:
            maxx = num
    
    return minn, maxx

random_numbers = random_list()
print("Згенерований список:", random_numbers)

minn, maxx = find(random_numbers)
print(f"Мінімальне значення: {minn}")
print(f"Максимальне значення: {maxx}")
