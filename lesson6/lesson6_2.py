import random


def a_plus_b(a, b, c):
    print(a + b * c)


a_plus_b(2, 2, 2)
a_plus_b(4, 4, 4)
a_plus_b(8, 8, 8)
a_plus_b(1000, 1000, 1000)


def pojalet_temirlana():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    result = int(input(f"Угадай результат этих чисел ({num1} * {num2})"))
    if result == num2 * num1:
        print("Ладнооооо, можно")
    elif result - 5 <= num2 * num1 <= result + 5:
        print("Было близко")
    else:
        print("Прости не твой день")


def kick_player(name):
    if name == "Temirlan":
        pojalet_temirlana()
    else:
        print(f"{name} вам можно")


def main(round):
    for i in range(round):
        name = input("Введите имя! ")
        kick_player(name)


round = int(input("Сколько раундов будешь играть Temirlan?"))
main(round)
