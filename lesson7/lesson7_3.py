def a_div_b(a, b=1):
    if b == 0:
        print("Нельзя делить на 0")
        b = 1
    c = a / b
    return c


c = a_div_b(a_div_b(4), a_div_b(10, 0))
print(c)

d = a_div_b(a=8, b=2)
print(d)
