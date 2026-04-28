# Задача 3. Оптимальний план виробництва

import subprocess
import sys

try:
    from scipy.optimize import linprog
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.optimize import linprog


print("=" * 55)
print("ОПТИМАЛЬНИЙ ПЛАН ВИРОБНИЦТВА")
print("=" * 55)


# --- 1. Формулювання задачі ---

print("\n1. ФОРМУЛЮВАННЯ ЗАДАЧІ")
print("-" * 45)
print("Змінні:")
print("  x - кількість стільців")
print("  y - кількість столів")
print("")
print("Цільова функція (максимізувати):")
print("  P(x, y) = 500x + 800y -> max")
print("")
print("Обмеження на ресурси:")
print("  Деревина:      2x + 4y <= 120")
print("  Робочий час:   3x + 2y <= 90")
print("")
print("Умови невід'ємності:")
print("  x >= 0")
print("  y >= 0")


# --- 2. Розв'язок через linprog ---

print("\n" + "=" * 55)
print("2. ПРОГРАМНИЙ РОЗВЯЗОК (linprog)")
print("-" * 45)
print("linprog мінімізує, тому мінімізуємо -P(x,y).")
print("Тобто коефіцієнти: [-500, -800]")
print("")

# Коефіцієнти цільової функції -P(x, y) = -500x - 800y
c = [-500, -800]

# Матриця обмежень A_ub * x <= b_ub
# Рядок 1: деревина    2x + 4y <= 120
# Рядок 2: робочий час 3x + 2y <= 90
A_ub = [
    [2, 4],
    [3, 2]
]

b_ub = [120, 90]

# Межі змінних: x >= 0, y >= 0
bounds = [(0, None), (0, None)]

result = linprog(
    c      = c,
    A_ub   = A_ub,
    b_ub   = b_ub,
    bounds = bounds,
    method = "highs"
)

x_opt = result.x[0]
y_opt = result.x[1]
profit = -result.fun

print("Результат linprog:")
print("  Стільців (x): " + str(round(x_opt, 2)))
print("  Столів   (y): " + str(round(y_opt, 2)))
print("")
print("Максимальний прибуток:")
print("  P = 500 * " + str(round(x_opt, 2)) + " + 800 * " + str(round(y_opt, 2)))
print("  P = " + str(round(500 * x_opt, 2)) + " + " + str(round(800 * y_opt, 2)))
print("  P = " + str(round(profit, 2)) + " грн")


# --- 3. Аналіз використання ресурсів ---

print("\n" + "=" * 55)
print("3. АНАЛІЗ ВИКОРИСТАННЯ РЕСУРСІВ")
print("-" * 45)

# Деревина
wood_used    = 2 * x_opt + 4 * y_opt
wood_total   = 120
wood_left    = wood_total - wood_used

# Робочий час
time_used    = 3 * x_opt + 2 * y_opt
time_total   = 90
time_left    = time_total - time_used

print("Деревина:")
print("  Використано: 2 * " + str(round(x_opt, 2)) + " + 4 * " + str(round(y_opt, 2)) + " = " + str(round(wood_used, 2)) + " м2")
print("  Запас:       " + str(wood_total) + " м2")
print("  Залишок:     " + str(round(wood_left, 2)) + " м2")

if wood_left < 0.01:
    print("  Ресурс використано ПОВНІСТЮ (активне обмеження)")
else:
    print("  Ресурс використано не повністю")

print("")
print("Робочий час:")
print("  Використано: 3 * " + str(round(x_opt, 2)) + " + 2 * " + str(round(y_opt, 2)) + " = " + str(round(time_used, 2)) + " год")
print("  Запас:       " + str(time_total) + " год")
print("  Залишок:     " + str(round(time_left, 2)) + " год")

if time_left < 0.01:
    print("  Ресурс використано ПОВНІСТЮ (активне обмеження)")
else:
    print("  Ресурс використано не повністю")

print("")
print("Висновок:")
if wood_left < 0.01 and time_left < 0.01:
    print("  Обидва ресурси використані повністю.")
    print("  Оптимальна точка знаходиться на перетині обох обмежень.")
elif wood_left < 0.01:
    print("  Деревина використана повністю, є залишок робочого часу.")
elif time_left < 0.01:
    print("  Робочий час використаний повністю, є залишок деревини.")
else:
    print("  Обидва ресурси мають залишок.")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("Стільців виготовити:  " + str(round(x_opt, 0)) + " шт.")
print("Столів виготовити:    " + str(round(y_opt, 0)) + " шт.")
print("Максимальний прибуток: " + str(round(profit, 2)) + " грн")
print("=" * 55)