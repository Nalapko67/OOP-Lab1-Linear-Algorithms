import math
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def main():
    print("--- Програма для обчислення математичних виразів ---")

    # Введення даних з клавіатури
    try:
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))
    except ValueError:
        print("Помилка: введено некоректні дані! Потрібно ввести числа.")
        return

    print(f"\n Введені дані: a = {a}, b = {b}\n")

    # 1. Обчислення z
    try:
        if a <= 0 or b <= 0 or b == 1:
            print("Помилка: логарифм log_b(a) не визначений при таких значеннях a та b!")
            return

        log_b_a = math.log(a) / math.log(b)
        denom_z = 1 + log_b_a

        if denom_z == 0:
            print("Помилка: знаменник при обчисленні z дорівнює 0!")
            return

        num_z = (math.atan(b - a) ** 3) + (b ** (1 / 3))
        z = num_z / denom_z
        print(f"z = {z:.6f}")
    except Exception as e:
        print(f"Помилка при розрахунку z: {e}")
        return

    # 2. Обчислення x
    try:
        ba_abs = abs(b * a)
        if ba_abs == 0:
            print("Помилка: аргумент логарифма b*a дорівнює 0!")
            return

        denom_x = 2 * math.log10(ba_abs)
        if denom_x == 0:
            print("Помилка: знаменник при обчисленні x дорівнює 0!")
            return

        num_x = math.exp(-2.5 * a) + math.sin(a**3)
        x = num_x / denom_x
        print(f"x = {x:.6f}")
    except Exception as e:
        print(f"Помилка при розрахунку x: {e}")
        return

    # 3. Обчислення y
    try:
        if x <= 0:
            print("Помилка: x <= 0, логарифм lg(x) не визначений!")
            return
        if z <= 0:
            print("Помилка: z <= 0, логарифм ln(z) не визначений!")
            return

        lg_x = math.log10(x)
        ln_z = math.log(z)

        y = -math.sqrt(abs(lg_x - ln_z) + 1)
        print(f"y = {y:.6f}")
    except Exception as e:
        print(f"Помилка при розрахунку y: {e}")
        return

    print("\n--- Підсумкові результати ---")
    print(f"x = {x:.6f}")
    print(f"y = {y:.6f}")
    print(f"z = {z:.6f}")


if __name__ == "__main__":
    main()