# Задача 1. Аналіз динаміки користувацької активності

import subprocess
import sys

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

try:
    from scipy.optimize import approx_fprime
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.optimize import approx_fprime

import math


# --- Основна функція f(t) = 1000 * t * e^(-0.2t) ---
def f(t):
    return 1000 * t * math.exp(-0.2 * t)


# --- Аналітична похідна f'(t) = 1000 * e^(-0.2t) * (1 - 0.2t) ---
# Правило добутку: (u * v)' = u' * v + u * v'
# u(t) = 1000t,       u'(t) = 1000
# v(t) = e^(-0.2t),   v'(t) = -0.2 * e^(-0.2t)
# f'(t) = 1000 * e^(-0.2t) + 1000t * (-0.2) * e^(-0.2t)
# f'(t) = 1000 * e^(-0.2t) * (1 - 0.2t)
def f_derivative(t):
    return 1000 * math.exp(-0.2 * t) * (1 - 0.2 * t)


# --- Переведення t у формат години:хвилини (початок 8:00) ---
def t_to_time(t):
    total_minutes = round(t * 60)
    hours = 8 + total_minutes // 60
    minutes = total_minutes % 60
    return str(hours) + ":" + str(minutes).zfill(2)


def main():
    print("=" * 60)
    print("АНАЛІЗ ДИНАМІКИ КОРИСТУВАЦЬКОІ АКТИВНОСТІ")
    print("=" * 60)

    # --- 1. Аналітична похідна ---
    print("\n1. АНАЛІТИЧНА ПОХІДНА")
    print("-" * 40)
    print("f(t)  = 1000 * t * e^(-0.2t)")
    print("")
    print("Застосовуємо правило добутку (u * v)' = u'*v + u*v':")
    print("  u(t)  = 1000t       =>  u'(t) = 1000")
    print("  v(t)  = e^(-0.2t)   =>  v'(t) = -0.2 * e^(-0.2t)")
    print("")
    print("f'(t) = 1000 * e^(-0.2t) + 1000t * (-0.2) * e^(-0.2t)")
    print("f'(t) = 1000 * e^(-0.2t) * (1 - 0.2t)")

    # --- 2. Пікове навантаження ---
    print("\n2. МОМЕНТ ПИКОВОГО НАВАНТАЖЕННЯ")
    print("-" * 40)
    print("Розвязуємо f'(t) = 0:")
    print("  1000 * e^(-0.2t) * (1 - 0.2t) = 0")
    print("  e^(-0.2t) ніколи не дорівнює 0")
    print("  Тому: 1 - 0.2t = 0")
    print("  t* = 1 / 0.2 = 5 годин")

    t_peak = 1 / 0.2
    peak_time = t_to_time(t_peak)
    peak_sessions = f(t_peak)

    print("")
    print("t* = " + str(t_peak) + " годин від початку робочого дня (8:00)")
    print("Час пікового навантаження: " + peak_time)
    print("Кількість сесій у пік: " + str(round(peak_sessions)))

    # --- 3. Чисельне диференціювання через approx_fprime ---
    print("\n3. ЧИСЕЛЬНЕ ДИФЕРЕНЦІЮВАННЯ (approx_fprime)")
    print("-" * 40)

    # approx_fprime очікує функцію від масиву, тому обгортаємо
    def f_for_scipy(t_array):
        return f(t_array[0])

    epsilon = [1e-6]
    moments = [2, 6, 10]

    numerical_results = {}
    for t in moments:
        derivative = approx_fprime([t], f_for_scipy, epsilon)[0]
        numerical_results[t] = derivative
        clock = t_to_time(t)
        print("t = " + str(t) + " (" + clock + ")  =>  f'(t) = " + str(round(derivative, 4)))

    # --- 4. Порівняння аналітичних та чисельних результатів ---
    print("\n4. ПОРІВНЯННЯ АНАЛІТИЧНИХ ТА ЧИСЕЛЬНИХ РЕЗУЛЬТАТИВ")
    print("-" * 60)
    print("t    Час    Аналіт.      Числовий     Різниця")
    print("-" * 60)

    for t in moments:
        analytic = f_derivative(t)
        numeric  = numerical_results[t]
        diff     = abs(analytic - numeric)
        clock    = t_to_time(t)
        print(
            "t=" + str(t) +
            "  " + clock +
            "  " + str(round(analytic, 4)) +
            "     " + str(round(numeric, 4)) +
            "     " + str(round(diff, 6))
        )

    print("")
    print("Висновок: різниця між методами мізерна (менше 0.001).")
    print("Обидва методи дають практично однаковий результат.")

    # --- 5. Інтерпретація для бізнесу ---
    print("\n5. ІНТЕРПРЕТАЦІЯ ДЛЯ БИЗНЕСУ")
    print("-" * 40)

    d_t2  = f_derivative(2)
    d_t6  = f_derivative(6)
    d_t10 = f_derivative(10)

    print("О 10:00 (t=2), f'(t) = " + str(round(d_t2, 2)) + "  (додатне)")
    print("  -> Активність зростає. IT-відділ має бути готовий")
    print("     до збільшення навантаження та мати резервні ресурси.")
    print("")
    print("О 14:00 (t=6), f'(t) = " + str(round(d_t6, 2)) + "  (майже нуль)")
    print("  -> Активність на плато, близько до максимуму.")
    print("")
    print("О 18:00 (t=10), f'(t) = " + str(round(d_t10, 2)) + "  (відємне)")
    print("  -> Активність спадає. Навантаження на сервери зменшується.")
    print("     Можна вимикати резервні потужності та економити ресурси.")
    print("")
    print("Рекомендація: максимальну кількість серверів тримати")
    print("о " + peak_time + " (t* = " + str(t_peak) + " год) - момент пікового навантаження.")

    print("=" * 60)


if __name__ == "__main__":
    main()