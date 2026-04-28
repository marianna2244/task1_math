# Задача 1. Оптимальна ціна товару

import subprocess
import sys

try:
    from scipy.optimize import minimize_scalar
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.optimize import minimize_scalar


# Функція попиту: Q(x) = 2000 - 0.8x
def Q(x):
    return 2000 - 0.8 * x


# Функція прибутку: P(x) = (x - 800) * Q(x)
def P(x):
    return (x - 800) * Q(x)


print("=" * 55)
print("ОПТИМАЛЬНА ЦІНА ТОВАРУ")
print("=" * 55)

print("\nВхідні дані:")
print("Попит:       Q(x) = 2000 - 0.8x")
print("Собівартість: 800 грн")
print("Прибуток:    P(x) = (x - 800) * (2000 - 0.8x)")


# --- 1. Критична точка аналітично ---

print("\n" + "=" * 55)
print("1. КРИТИЧНА ТОЧКА АНАЛІТИЧНО")
print("-" * 45)
print("Розкриваємо дужки:")
print("P(x) = (x - 800) * (2000 - 0.8x)")
print("P(x) = 2000x - 0.8x^2 - 1600000 + 640x")
print("P(x) = -0.8x^2 + 2640x - 1600000")
print("")
print("Обчислюємо похідну P'(x):")
print("P'(x) = -1.6x + 2640")
print("")
print("Прирівнюємо до нуля: P'(x) = 0")
print("-1.6x + 2640 = 0")
print("1.6x = 2640")
print("x* = 2640 / 1.6")

x_analytic = 2640 / 1.6

print("x* = " + str(x_analytic) + " грн")


# --- 2. Тип екстремуму ---

print("\n" + "=" * 55)
print("2. ТИП ЕКСТРЕМУМУ")
print("-" * 45)
print("Обчислюємо другу похідну P''(x):")
print("P'(x)  = -1.6x + 2640")
print("P''(x) = -1.6")
print("")
print("P''(x) = -1.6 < 0 для будь-якого x")
print("")
print("Оскільки P''(x) < 0, функція прибутку")
print("є угнутою, а критична точка x* = " + str(x_analytic) + " грн")
print("є точкою МАКСИМУМУ.")


# --- 3. Чисельний розв'язок через minimize_scalar ---

print("\n" + "=" * 55)
print("3. ЧИСЕЛЬНИЙ РОЗВЯЗОК (minimize_scalar)")
print("-" * 45)
print("minimize_scalar шукає мінімум,")
print("тому мінімізуємо -P(x) для знаходження максимуму P(x).")
print("")

result = minimize_scalar(
    fun    = lambda x: -P(x),
    bounds = (800, 2500),
    method = "bounded"
)

x_numeric = result.x

print("Інтервал пошуку: [800, 2500]")
print("Результат minimize_scalar:")
print("x* = " + str(round(x_numeric, 4)) + " грн")


# --- 4. Порівняння та обчислення прибутку ---

print("\n" + "=" * 55)
print("4. ПОРІВНЯННЯ РЕЗУЛЬТАТІВ ТА ПРИБУТОК")
print("-" * 45)

diff = abs(x_analytic - x_numeric)

print("Аналітичний результат: x* = " + str(x_analytic) + " грн")
print("Чисельний результат:   x* = " + str(round(x_numeric, 4)) + " грн")
print("Різниця: " + str(round(diff, 6)) + " грн")
print("")

if diff < 0.01:
    print("Результати збігаються.")

print("")
print("Обчислюємо максимальний прибуток при x* = " + str(x_analytic) + " грн:")
print("")

q_optimal = Q(x_analytic)
profit_optimal = P(x_analytic)

print("Q(x*) = 2000 - 0.8 * " + str(x_analytic))
print("Q(x*) = " + str(q_optimal) + " одиниць")
print("")
print("P(x*) = (x* - 800) * Q(x*)")
print("P(x*) = (" + str(x_analytic) + " - 800) * " + str(q_optimal))
print("P(x*) = " + str(x_analytic - 800) + " * " + str(q_optimal))
print("P(x*) = " + str(round(profit_optimal, 2)) + " грн")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("Оптимальна ціна:         " + str(x_analytic) + " грн")
print("Кількість продажів:      " + str(int(q_optimal)) + " одиниць")
print("Максимальний прибуток:   " + str(round(profit_optimal, 2)) + " грн/міс")
print("=" * 55)