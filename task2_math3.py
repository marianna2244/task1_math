# Задача 2. Моделювання процесу навчання

import subprocess
import sys

try:
    from scipy.integrate import solve_ivp
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.integrate import solve_ivp

import math

# Параметри моделі
M = 100   # максимальний рівень знань (%)
r = 0.15  # коефіцієнт швидкості навчання


# --- 1. Функція моделі ---
# Права частина диференціального рівняння dK/dt = r * (M - K)
def learning_rate(t, K):
    return [r * (M - K[0])]


# --- Допоміжна функція: знайти день коли досягнуто 90% ---
def find_day_90_percent(times, values):
    for i in range(len(values)):
        if values[i] >= 90:
            return round(times[i], 1)
    return None


def main():
    print("=" * 55)
    print("МОДЕЛЮВАННЯ ПРОЦЕСУ НАВЧАННЯ")
    print("=" * 55)

    # --- 2. Розвязання рівняння для K(0) = 10 ---
    print("\n1. ФУНКЦІЯ МОДЕЛІ")
    print("-" * 40)
    print("dK/dt = r * (M - K)")
    print("r = " + str(r) + ",  M = " + str(M))
    print("Чим менше знань залишилось засвоїти,")
    print("тим повільніше студент вчиться.")

    print("\n2. ЧИСЕЛЬНИЙ РОЗВЯЗОК для K(0) = 10")
    print("-" * 40)

    t_start = 0
    t_end   = 30
    K0      = [10]

    solution = solve_ivp(
        fun      = learning_rate,
        t_span   = (t_start, t_end),
        y0       = K0,
        dense_output = True
    )

    # Виводимо значення кожні 5 днів
    print("День   Рівень знань (%)")
    print("-" * 30)
    for day in range(0, 31, 5):
        value = solution.sol(day)[0]
        print("День " + str(day) + ":  " + str(round(value, 2)) + "%")

    # --- 3. Порівняння трьох студентів ---
    print("\n3. ПОРІВНЯННЯ СТУДЕНТИВ З РІЗНИМ ПОЧАТКОВИМ РІВНЕМ")
    print("-" * 55)

    initial_levels = [5, 10, 20]

    for k_start in initial_levels:
        sol = solve_ivp(
            fun      = learning_rate,
            t_span   = (0, 60),
            y0       = [k_start],
            dense_output = True
        )

        # Шукаємо день досягнення 90%
        days = [i * 0.1 for i in range(601)]
        values = [sol.sol(d)[0] for d in days]

        day_90 = find_day_90_percent(days, values)

        print("Початковий рівень: " + str(k_start) + "%")
        print("  Рівень на 10-й день: " + str(round(sol.sol(10)[0], 2)) + "%")
        print("  Рівень на 20-й день: " + str(round(sol.sol(20)[0], 2)) + "%")
        print("  Рівень на 30-й день: " + str(round(sol.sol(30)[0], 2)) + "%")

        if day_90 is not None:
            print("  90% знань досягнуто на день: " + str(day_90))
        else:
            print("  90% знань не досягнуто за 60 днів")
        print("")

    # --- Висновок ---
    print("-" * 55)
    print("ВИСНОВОК:")
    print("")
    print("Студент з K(0)=5  досягає 90% пізніше за всіх.")
    print("Студент з K(0)=10 досягає 90% швидше ніж перший.")
    print("Студент з K(0)=20 досягає 90% найшвидше.")
    print("")
    print("Чим вища початкова підготовка студента,")
    print("тим швидше він досягає високого рівня знань.")
    print("Різниця між K(0)=5 та K(0)=20 складає кілька днів,")
    print("що підтверджує важливість базових знань перед курсом.")

    print("=" * 55)


if __name__ == "__main__":
    main()