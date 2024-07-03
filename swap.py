def swap():
    input_string = str(input("Введіть рядок: "))
    rezult = ''
    for i in input_string:
        if i.islower():
            rezult += i.upper()
        elif i.isupper():
            rezult += i.lower()
    print("Змінений рядок ", rezult)

swap()
