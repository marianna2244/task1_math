# Задача 2. Мінімізація функції двох змінних

import subprocess
import sys

try:
    from scipy.optimize import minimize
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.optimize import minimize

import math


# Функція f(x, y) = x^2 + xy + y^2 - 6x - 9y + 20
def f(point):
    x = point[0]
    y = point[1]
    return x**2 + x*y + y**2 - 6*x - 9*y + 20


print("=" * 55)
print("МІНІМІЗАЦІЯ ФУНКЦІЇ ДВОХ ЗМІННИХ")
print("=" * 55)
print("\nf(x,y) = x^2 + xy + y^2 - 6x - 9y + 20")


# --- 1. Критична точка аналітично ---

print("\n" + "=" * 55)
print("1. КРИТИЧНА ТОЧКА АНАЛІТИЧНО")
print("-" * 45)
print("Частинні похідні:")
print("")
print("df/dx: диференціюємо по x, y вважаємо константою:")
print("  x^2  -> 2x")
print("  xy   -> y")
print("  y^2  -> 0")
print("  -6x  -> -6")
print("  -9y  -> 0")
print("  df/dx = 2x + y - 6")
print("")
print("df/dy: диференціюємо по y, x вважаємо константою:")
print("  x^2  -> 0")
print("  xy   -> x")
print("  y^2  -> 2y")
print("  -6x  -> 0")
print("  -9y  -> -9")
print("  df/dy = x + 2y - 9")
print("")
print("Прирівнюємо до нуля - система рівнянь:")
print("  2x + y  = 6   ... (1)")
print("  x  + 2y = 9   ... (2)")
print("")
print("Розв'язок системи:")
print("  З (1): y = 6 - 2x")
print("  Підставляємо в (2): x + 2*(6 - 2x) = 9")
print("  x + 12 - 4x = 9")
print("  -3x = -3")
print("  x* = 1")
print("  y* = 6 - 2*1 = 4")

x_star = 1
y_star = 4
f_star = f([x_star, y_star])

print("")
print("Критична точка: (" + str(x_star) + ", " + str(y_star) + ")")
print("f(x*, y*) = " + str(f_star))


# --- 2. Тип екстремуму через матрицю Гессе ---

print("\n" + "=" * 55)
print("2. ТИП ЕКСТРЕМУМУ - МАТРИЦЯ ГЕССЕ")
print("-" * 45)
print("Другі частинні похідні:")
print("")
print("d^2f/dx^2  = 2   (похідна від 2x + y - 6 по x)")
print("d^2f/dy^2  = 2   (похідна від x + 2y - 9 по y)")
print("d^2f/dxdy  = 1   (похідна від 2x + y - 6 по y)")
print("")
print("Матриця Гессе H:")
print("  H = | 2  1 |")
print("      | 1  2 |")
print("")
print("Характеристичне рівняння det(H - lambda*I) = 0:")
print("  | 2-lambda    1     |")
print("  |    1     2-lambda | = 0")
print("")
print("  (2 - lambda)^2 - 1*1 = 0")
print("  4 - 4*lambda + lambda^2 - 1 = 0")
print("  lambda^2 - 4*lambda + 3 = 0")
print("  (lambda - 1) * (lambda - 3) = 0")

lambda1 = 1
lambda2 = 3

print("")
print("Власні значення:")
print("  lambda1 = " + str(lambda1))
print("  lambda2 = " + str(lambda2))
print("")
print("Обидва власних значення > 0:")
print("  lambda1 = " + str(lambda1) + " > 0")
print("  lambda2 = " + str(lambda2) + " > 0")
print("")
print("Матриця Гессе є додатньо визначеною.")
print("Критична точка (1, 4) є точкою МІНІМУМУ.")


# --- 3. Чисельний розв'язок через minimize з BFGS ---

print("\n" + "=" * 55)
print("3. ЧИСЕЛЬНИЙ РОЗВЯЗОК (BFGS)")
print("-" * 45)
print("Початкова точка: (0, 0)")
print("")

result = minimize(f, x0=[0, 0], method="BFGS")

x_numeric = result.x[0]
y_numeric = result.x[1]
f_numeric = result.fun

print("Результат minimize (BFGS):")
print("x* = " + str(round(x_numeric, 6)))
print("y* = " + str(round(y_numeric, 6)))
print("f(x*, y*) = " + str(round(f_numeric, 6)))
print("")

diff_x = abs(x_star - x_numeric)
diff_y = abs(y_star - y_numeric)

print("Різниця з аналітичним розв'язком:")
print("  dx = " + str(round(diff_x, 8)))
print("  dy = " + str(round(diff_y, 8)))

if diff_x < 0.0001 and diff_y < 0.0001:
    print("Результати збігаються.")


# --- 4. Стійкість розв'язку ---

print("\n" + "=" * 55)
print("4. СТІЙКІСТЬ РОЗВЯЗКУ")
print("-" * 45)
print("Запускаємо оптимізацію з трьох різних точок:")
print("")

start_points = [
    [0, 0],
    [10, 10],
    [-5, 15]
]

all_converge = True

for start in start_points:
    res = minimize(f, x0=start, method="BFGS")
    rx = round(res.x[0], 4)
    ry = round(res.x[1], 4)
    rf = round(res.fun, 4)

    print("Старт (" + str(start[0]) + ", " + str(start[1]) + ")  ->  " +
          "x* = " + str(rx) + ",  y* = " + str(ry) + ",  f = " + str(rf))

    if abs(res.x[0] - x_star) > 0.01 or abs(res.x[1] - y_star) > 0.01:
        all_converge = False

print("")
if all_converge:
    print("Всі три запуски збіглися до точки (" + str(x_star) + ", " + str(y_star) + ").")
    print("Розв'язок є стійким - мінімум глобальний.")
else:
    print("Увага: запуски дали різні результати.")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("Критична точка:   (" + str(x_star) + ", " + str(y_star) + ")")
print("Тип екстремуму:   мінімум (lambda1=1 > 0, lambda2=3 > 0)")
print("Мінімальне f:     " + str(f_star))
print("=" * 55)