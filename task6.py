#todo: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().

def square(a):
    return (a ** 2)

if __name__ == "__main__":
    a = int(input("Введите длину стороны квадрата: "))
    print(f"Площадь квадрата равна {square(a)}")

