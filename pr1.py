import math
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


# Функція для обчислення дійсного кубічного кореня
def cbrt(val):
    if val >= 0:
        return val ** (1 / 3)
    else:
        return -((-val) ** (1 / 3))


try:
    # 1. Введення значення x з клавіатури
    x = float(input("Введіть значення x = "))

    # 2. Перевірка ОДЗ для натурального логарифма
    if x <= 0:
        print(
            "Помилка: x має бути більше 0, оскільки натуральний логарифм ln(x) визначений тільки для додатних чисел!"
        )
    else:
        # 3. Обчислення чисельника: sin(x^2) - cos^4((x-1)^2)
        numerator = math.sin(x**2) - (math.cos((x - 1) ** 2)) ** 4

        # 4. Обчислення знаменника: arctg(x + 2.6) + root3(ln(x))
        ln_val = math.log(x)
        denominator = math.atan(x + 2.6) + cbrt(ln_val)

        # 5. Перевірка на ділення на нуль
        if denominator == 0:
            print("Помилка: знаменник дорівнює 0 (ділення на нуль неможливе)!")
        else:
            # Обчислення результату
            g = numerator / denominator
            print(f"Результат: g = {g:.6f}")

except ValueError:
    print("Помилка: введено некоректні дані! Будь ласка, введіть число.")