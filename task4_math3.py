# Задача 4. Аналіз функції двох змінних

import subprocess
import sys

try:
    from scipy.optimize import approx_fprime
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.optimize import approx_fprime


def f(x, y):
    return 0.5 * x**2 + 0.3 * y**2 + 0.2 * x * y + 10 * x + 5 * y


def df_dx(x, y):
    return x + 0.2 * y + 10


def df_dy(x, y):
    return 0.6 * y + 0.2 * x + 5


def f_for_scipy(point):
    return f(point[0], point[1])


print("=" * 55)
print("АНАЛІЗ ФУНКЦІЇ ДВОХ ЗМІННИХ")
print("=" * 55)


# --- 1. Аналітичні часткові похідні ---

print("\n1. ЧАСТКОВІ ПОХІДНІ АНАЛІТИЧНО")
print("-" * 45)
print("f(x,y) = 0.5x^2 + 0.3y^2 + 0.2xy + 10x + 5y")
print("")
print("df/dx: диференціюємо по x, y вважаємо константою:")
print("  0.5x^2 -> x")
print("  0.3y^2 -> 0")
print("  0.2xy  -> 0.2y")
print("  10x    -> 10")
print("  5y     -> 0")
print("  df/dx = x + 0.2y + 10")
print("")
print("df/dy: диференціюємо по y, x вважаємо константою:")
print("  0.5x^2 -> 0")
print("  0.3y^2 -> 0.6y")
print("  0.2xy  -> 0.2x")
print("  10x    -> 0")
print("  5y     -> 5")
print("  df/dy = 0.6y + 0.2x + 5")


# --- 2. Чисельний градієнт ---

print("\n2. ЧИСЕЛЬНИЙ ГРАДІЄНТ У ТОЧЦІ (10, 20)")
print("-" * 45)

point = [10, 20]
epsilon = [1e-6, 1e-6]

gradient = approx_fprime(point, f_for_scipy, epsilon)

print("Точка: x = 10,  y = 20")
print("")
print("Чисельний градієнт:")
print("  df/dx = " + str(round(gradient[0], 6)))
print("  df/dy = " + str(round(gradient[1], 6)))


# --- 3. Порівняння методів ---

print("\n3. ПОРІВНЯННЯ МЕТОДІВ У ТОЧЦІ (10, 20)")
print("-" * 45)

x0 = 10
y0 = 20

analytic_dx = df_dx(x0, y0)
analytic_dy = df_dy(x0, y0)

numeric_dx = gradient[0]
numeric_dy = gradient[1]

diff_dx = abs(analytic_dx - numeric_dx)
diff_dy = abs(analytic_dy - numeric_dy)

print("          Аналітично    Чисельно     Різниця")
print("-" * 45)
print("df/dx:    " + str(round(analytic_dx, 4)) + "          " + str(round(numeric_dx, 4)) + "      " + str(round(diff_dx, 8)))
print("df/dy:    " + str(round(analytic_dy, 4)) + "          " + str(round(numeric_dy, 4)) + "      " + str(round(diff_dy, 8)))
print("")
print("Різниця між методами практично нульова.")
print("Обидва методи дають однаковий результат.")


# --- 4. Лінійна апроксимація ---

print("\n4. ЛІНІЙНА АПРОКСИМАЦІЯ ЗМІНИ ФУНКЦІЇ")
print("-" * 45)

dx = 0.5
dy = -0.3

print("Точка: (10, 20)")
print("Зміни: dx = " + str(dx) + ",  dy = " + str(dy))
print("")
print("Формула: df = (df/dx) * dx + (df/dy) * dy")
print("")

delta_f_approx = analytic_dx * dx + analytic_dy * dy

print("df = " + str(analytic_dx) + " * " + str(dx) + " + " + str(analytic_dy) + " * " + str(dy))
print("df = " + str(analytic_dx * dx) + " + (" + str(analytic_dy * dy) + ")")
print("df = " + str(round(delta_f_approx, 6)))

f_original = f(10, 20)
f_new = f(10 + dx, 20 + dy)
delta_f_exact = f_new - f_original

print("")
print("Точна зміна:")
print("  f(10, 20)      = " + str(round(f_original, 6)))
print("  f(10.5, 19.7)  = " + str(round(f_new, 6)))
print("  Точна зміна    = " + str(round(delta_f_exact, 6)))

print("")
print("Наближена зміна: " + str(round(delta_f_approx, 6)))
print("Точна зміна:     " + str(round(delta_f_exact, 6)))
print("Різниця:         " + str(round(abs(delta_f_approx - delta_f_exact), 6)))
print("")
print("Лінійна апроксимація дає дуже точний")
print("результат для малих змін dx та dy.")

print("=" * 55)