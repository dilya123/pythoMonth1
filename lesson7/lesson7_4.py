def int_input():
    while True:
        try:
            age = int(input())
            return age
        except ValueError:
            print("Введите число")


age = int_input()
print(age)
