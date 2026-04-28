# Задача 3. Аналіз ефективності рекламної кампанії

import subprocess
import sys

try:
    from scipy.integrate import quad
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.integrate import quad

import math


# Функція інтенсивності реєстрацій f(t) = 500 * e^(-0.3t)
def f(t):
    return 500 * math.exp(-0.3 * t)


def main():
    print("=" * 55)
    print("АНАЛІЗ ЕФЕКТИВНОСТІ РЕКЛАМНОЇ КАМПАНІЇ")
    print("=" * 55)

    # --- 1. Аналітичний інтеграл за 7 днів ---
    # Первісна: F(t) = 500 * (1 / -0.3) * e^(-0.3t) = -1666.67 * e^(-0.3t)
    # Інтеграл від 0 до 7 = F(7) - F(0)

    print("\n1. АНАЛІТИЧНИЙ ІНТЕГРАЛ (0 до 7 днів)")
    print("-" * 45)
    print("f(t) = 500 * e^(-0.3t)")
    print("")
    print("Первісна: F(t) = 500 * (1 / -0.3) * e^(-0.3t)")
    print("          F(t) = -1666.67 * e^(-0.3t)")
    print("")
    print("За формулою Ньютона-Лейбніца:")
    print("Integral = F(7) - F(0)")

    coeff = 500 / (-0.3)  # = -1666.67

    F_7 = coeff * math.exp(-0.3 * 7)
    F_0 = coeff * math.exp(-0.3 * 0)

    analytic_7 = F_7 - F_0

    print("")
    print("F(7) = -1666.67 * e^(-2.1) = " + str(round(F_7, 4)))
    print("F(0) = -1666.67 * e^(0)    = " + str(round(F_0, 4)))
    print("")
    print("Integral = " + str(round(F_7, 4)) + " - (" + str(round(F_0, 4)) + ")")
    print("Аналітичний результат: " + str(round(analytic_7, 2)) + " реєстрацій")

    # --- 2. Чисельна перевірка через quad ---
    print("\n2. ЧИСЕЛЬНА ПЕРЕВІРКА (quad)")
    print("-" * 45)

    numeric_7, error = quad(f, 0, 7)

    print("Результат quad: " + str(round(numeric_7, 2)) + " реєстрацій")
    print("Похибка quad:   " + str(round(error, 8)))
    print("")

    diff = abs(analytic_7 - numeric_7)
    print("Різниця між методами: " + str(round(diff, 6)))

    if diff < 0.01:
        print("Результати збігаються. Перевірку пройдено.")
    else:
        print("Увага: результати відрізняються!")

    # --- 3. Невласний інтеграл (теоретичний максимум) ---
    # При t -> нескінченність: e^(-0.3t) -> 0
    # Integral від 0 до inf = F(inf) - F(0) = 0 - (-1666.67) = 1666.67

    print("\n3. ТЕОРЕТИЧНИЙ МАКСИМУМ (інтеграл від 0 до нескінченності)")
    print("-" * 45)
    print("При t -> нескінченність: e^(-0.3t) -> 0")
    print("F(inf) = -1666.67 * 0 = 0")
    print("F(0)   = -1666.67 * 1 = " + str(round(F_0, 2)))
    print("")

    analytic_inf = 0 - F_0

    print("Аналітично: 0 - (" + str(round(F_0, 2)) + ") = " + str(round(analytic_inf, 2)))

    # Перевірка через quad з великим верхнім обмеженням
    numeric_inf, error_inf = quad(f, 0, math.inf)
    print("Через quad:  " + str(round(numeric_inf, 2)))
    print("")
    print("Теоретичний максимум реєстрацій: " + str(round(analytic_inf, 2)))

    # --- 4. Ефективність першого тижня ---
    print("\n4. ЕФЕКТИВНІСТЬ ПЕРШОГО ТИЖНЯ")
    print("-" * 45)

    efficiency = (analytic_7 / analytic_inf) * 100

    print("Реєстрацій за 7 днів:        " + str(round(analytic_7, 2)))
    print("Теоретичний максимум:         " + str(round(analytic_inf, 2)))
    print("Ефективність першого тижня:   " + str(round(efficiency, 2)) + "%")
    print("")
    print("Висновок:")
    print("За перший тиждень збирається " + str(round(efficiency, 1)) + "% від усіх")
    print("можливих реєстрацій. Перший тиждень є ключовим")
    print("для охоплення аудиторії - більше половини потенційних")
    print("студентів реєструються саме в цей період.")

    print("=" * 55)


if __name__ == "__main__":
    main()