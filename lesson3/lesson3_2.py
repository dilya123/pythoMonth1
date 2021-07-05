name = input()
age = int(input())
hobby = input()

if name == "Aман" and age >= 16 and hobby == "плавать":
    print("Прветствую хозяин!")
    login = input()
    password = input()
    if login == "soulunthesoil" and password == "rysyk19816767":
        print("Хозяин залогинился!")
    else:
        print("Не правильный логин и пароль!")
else:
    print("Вы не хозяин!")


if name == "Aман" or age >= 16 or hobby == "плавать":
    print("Вы либо Аман, либо вам больше 16, либо вы любите плавать")
else:
    print("Вы не подходите вообще!")
