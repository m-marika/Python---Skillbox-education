# TODO здесь писать код
def include_circle(x, y, r):
    if abs(x) <= r and abs(y) <= r:
        print("\nМонетка где-то рядом")
    else:
        print("\nМонетки в области нет")


print("Введите координаты монетки:")
x_coin = float(input("x: "))
y_coin = float(input("y: "))
r_circle = float(input("Введите радиус: "))

include_circle(x_coin, y_coin, r_circle)

# зачтено
