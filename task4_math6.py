# Задача 4. Комплексний аналіз виробництва

import subprocess
import sys

try:
    import numpy as np
    from scipy.optimize import approx_fprime, minimize_scalar, minimize
    from scipy.integrate import quad
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy", "scipy"])
    import numpy as np
    from scipy.optimize import approx_fprime, minimize_scalar, minimize
    from scipy.integrate import quad


# Функція продуктивності P(t) = 100 + 40t - 4t^2
def P(t):
    return 100 + 40 * t - 4 * t**2


# Функція вартості C(x, y) = x^2 + y^2 - 10x - 8y + 50
def C(point):
    x = point[0]
    y = point[1]
    return x**2 + y**2 - 10*x - 8*y + 50


print("=" * 55)
print("КОМПЛЕКСНИЙ АНАЛІЗ ВИРОБНИЦТВА")
print("=" * 55)
print("")
print("P(t) = 100 + 40t - 4t^2")
print("C(x,y) = x^2 + y^2 - 10x - 8y + 50")


# ============================================================
# ЧАСТИНА 1. ДОСЛІДЖЕННЯ ПРОДУКТИВНОСТІ
# ============================================================

print("\n" + "=" * 55)
print("ЧАСТИНА 1. ДОСЛІДЖЕННЯ ПРОДУКТИВНОСТІ")
print("=" * 55)


# --- 1. Динаміка продуктивності через approx_fprime ---

print("\n1. ШВИДКІСТЬ ЗМІНИ ПРОДУКТИВНОСТІ P'(t)")
print("-" * 45)
print("Використовуємо approx_fprime для обчислення P'(t)")
print("")

def P_for_scipy(t_array):
    return P(t_array[0])

moments = [2, 5, 8]
epsilon = [1e-6]

print("t    P(t)        P'(t)       Висновок")
print("-" * 50)

for t in moments:
    p_val    = P(t)
    p_deriv  = approx_fprime([t], P_for_scipy, epsilon)[0]

    if p_deriv > 0:
        conclusion = "зростає"
    elif p_deriv < 0:
        conclusion = "спадає"
    else:
        conclusion = "максимум"

    print(
        "t=" + str(t) + "  " +
        str(round(p_val, 2)) + "      " +
        str(round(p_deriv, 4)) + "      " +
        conclusion
    )


# --- 2. Момент пікової продуктивності ---

print("\n2. ПІКОВА ПРОДУКТИВНІСТЬ (minimize_scalar)")
print("-" * 45)
print("Мінімізуємо -P(t) для знаходження максимуму P(t).")
print("")

result_peak = minimize_scalar(
    fun    = lambda t: -P(t),
    bounds = (0, 10),
    method = "bounded"
)

t_peak = result_peak.x
p_peak = P(t_peak)

print("t* = " + str(round(t_peak, 4)) + " год")
print("P(t*) = " + str(round(p_peak, 4)) + " одиниць/год")
print("")
print("Аналітична перевірка: P'(t) = 40 - 8t = 0  =>  t* = 5")


# --- 3. Загальний обсяг виробництва через quad ---

print("\n3. ЗАГАЛЬНИЙ ОБСЯГ ВИРОБНИЦТВА (quad)")
print("-" * 45)
print("Обчислюємо інтеграл від 0 до 10: integral P(t) dt")
print("")

total_volume, error = quad(P, 0, 10)

print("Integral(0 до 10) P(t) dt = " + str(round(total_volume, 2)) + " одиниць")
print("Похибка обчислення:        " + str(round(error, 8)))
print("")
print("Аналітична перевірка:")
print("Integral(100 + 40t - 4t^2) dt = 100t + 20t^2 - (4/3)t^3")
analytic = 100*10 + 20*100 - (4/3)*1000
print("F(10) - F(0) = " + str(round(analytic, 2)))


# ============================================================
# ЧАСТИНА 2. ОПТИМІЗАЦІЯ ВИТРАТ
# ============================================================

print("\n" + "=" * 55)
print("ЧАСТИНА 2. ОПТИМІЗАЦІЯ ВИТРАТ")
print("=" * 55)


# --- 4. Початкові параметри через linalg.solve ---

print("\n4. ПОЧАТКОВІ ПАРАМЕТРИ (linalg.solve)")
print("-" * 45)
print("Система рівнянь:")
print("  2x + y  = 20")
print("  x  + 3y = 25")
print("")

A = np.array([
    [2, 1],
    [1, 3]
])
b = np.array([20, 25])

x0_y0 = np.linalg.solve(A, b)
x0 = x0_y0[0]
y0 = x0_y0[1]

print("Розв'язок системи:")
print("x0 = " + str(round(x0, 4)))
print("y0 = " + str(round(y0, 4)))
print("")
print("C(x0, y0) = " + str(round(C([x0, y0]), 4)) + " грн")


# --- 5. Мінімізація вартості через minimize BFGS ---

print("\n5. МІНІМІЗАЦІЯ ВАРТОСТІ (minimize BFGS)")
print("-" * 45)
print("Початкова точка: (" + str(round(x0, 4)) + ", " + str(round(y0, 4)) + ")")
print("")

result_cost = minimize(C, x0=[x0, y0], method="BFGS")

x_opt = result_cost.x[0]
y_opt = result_cost.x[1]
c_min = result_cost.fun

print("Оптимальні параметри:")
print("x* = " + str(round(x_opt, 4)))
print("y* = " + str(round(y_opt, 4)))
print("C(x*, y*) = " + str(round(c_min, 4)) + " грн")
print("")
print("Аналітична перевірка:")
print("dC/dx = 2x - 10 = 0  =>  x* = 5")
print("dC/dy = 2y - 8  = 0  =>  y* = 4")
print("C(5, 4) = 25 + 16 - 50 - 32 + 50 = " + str(C([5, 4])))


# ============================================================
# ФІНАЛ
# ============================================================

print("\n" + "=" * 55)
print("ФІНАЛ. ЗАГАЛЬНА ВАРТІСТЬ ВИРОБНИЦТВА")
print("=" * 55)

total_cost = total_volume * c_min

print("")
print("Загальний обсяг:      " + str(round(total_volume, 2)) + " одиниць")
print("Мінімальна вартість:  " + str(round(c_min, 4)) + " грн/одиниця")
print("")
print("Загальна вартість = обсяг * вартість одиниці")
print("Загальна вартість = " + str(round(total_volume, 2)) + " * " + str(round(c_min, 4)))
print("Загальна вартість = " + str(round(total_cost, 2)) + " грн")

print("\n" + "=" * 55)
print("ПІДСУМОК PIPELINE")
print("=" * 55)
print("1. P'(2)=24 зростає, P'(5)=0 максимум, P'(8)=-24 спадає")
print("2. Пік продуктивності: t* = " + str(round(t_peak, 2)) + " год, P = " + str(round(p_peak, 2)))
print("3. Обсяг за зміну:     " + str(round(total_volume, 2)) + " одиниць")
print("4. Початкові витрати:  x0=" + str(round(x0, 2)) + ", y0=" + str(round(y0, 2)))
print("5. Мінімальна вартість: C(5,4) = " + str(round(c_min, 2)) + " грн")
print("6. Загальна вартість:   " + str(round(total_cost, 2)) + " грн")
print("=" * 55)