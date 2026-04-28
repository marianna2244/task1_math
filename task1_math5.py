# Задача 1. Аналіз рейтингів мобільного додатку

import subprocess
import sys

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# Вхідні дані
scores = np.array([1, 2, 3, 4, 5])
counts = np.array([120, 180, 320, 580, 800])
total  = counts.sum()

print("=" * 50)
print("АНАЛІЗ РЕЙТИНГІВ МОБІЛЬНОГО ДОДАТКУ")
print("=" * 50)

print("\nВхідні дані:")
print("Загальна кількість відгуків: " + str(total))


# --- 1. PMF ---

pmf = counts / total


# --- 2. CDF ---

cdf = np.cumsum(pmf)


# --- 3. Таблиця PMF та CDF ---

print("\nОцінка | PMF (P(X=x)) | CDF (P(X<=x))")
print("-" * 42)
for i in range(len(scores)):
    print(
        "  " + str(scores[i]) + "    |   " +
        str(round(pmf[i], 4)) + "       |   " +
        str(round(cdf[i], 4))
    )


# --- 4. Математичне сподівання, дисперсія, стандартне відхилення ---

print("\n" + "=" * 50)
print("ЧИСЛОВІ ХАРАКТЕРИСТИКИ")
print("=" * 50)

# E[X] = сума x * P(X=x)
ex = np.sum(scores * pmf)

# E[X^2] = сума x^2 * P(X=x)
ex2 = np.sum(scores**2 * pmf)

# Var(X) = E[X^2] - (E[X])^2
var = ex2 - ex**2

# Стандартне відхилення
sigma = np.sqrt(var)

print("\nE[X]   = сума( x * P(X=x) )")
print("E[X]   = " + str(round(ex, 4)))

print("\nE[X^2] = сума( x^2 * P(X=x) )")
print("E[X^2] = " + str(round(ex2, 4)))

print("\nVar(X) = E[X^2] - (E[X])^2")
print("Var(X) = " + str(round(ex2, 4)) + " - " + str(round(ex**2, 4)))
print("Var(X) = " + str(round(var, 4)))

print("\nСтандартне відхилення = sqrt(Var(X))")
print("sigma  = " + str(round(sigma, 4)))


# --- 5. Ймовірність негативної оцінки (1 або 2 зірки) ---

print("\n" + "=" * 50)
print("ЙМОВІРНОСТІ")
print("=" * 50)

p_negative = pmf[0] + pmf[1]

print("\nЙмовірність негативної оцінки (1 або 2 зірки):")
print("P(X <= 2) = P(X=1) + P(X=2)")
print("P(X <= 2) = " + str(round(pmf[0], 4)) + " + " + str(round(pmf[1], 4)))
print("P(X <= 2) = " + str(round(p_negative, 4)))
print("P(X <= 2) = " + str(round(p_negative * 100, 2)) + "%")


# --- 6. Ймовірність високої оцінки (4 або більше зірок) ---

p_high = pmf[3] + pmf[4]

print("\nЙмовірність високої оцінки (4 або 5 зірок):")
print("P(X >= 4) = P(X=4) + P(X=5)")
print("P(X >= 4) = " + str(round(pmf[3], 4)) + " + " + str(round(pmf[4], 4)))
print("P(X >= 4) = " + str(round(p_high, 4)))
print("P(X >= 4) = " + str(round(p_high * 100, 2)) + "%")


# --- 7. Медіана ---

print("\nМедіана рейтингу:")
print("Шукаємо найменше x де CDF(x) >= 0.5")
print("")

median = None
for i in range(len(scores)):
    print("CDF(" + str(scores[i]) + ") = " + str(round(cdf[i], 4)))
    if median is None and cdf[i] >= 0.5:
        median = scores[i]

print("\nМедіана = " + str(median))


print("\n" + "=" * 50)
print("ПІДСУМОК")
print("=" * 50)
print("Математичне сподівання E[X]: " + str(round(ex, 4)))
print("Дисперсія Var(X):            " + str(round(var, 4)))
print("Стандартне відхилення sigma: " + str(round(sigma, 4)))
print("P(негативна оцінка):         " + str(round(p_negative * 100, 2)) + "%")
print("P(висока оцінка >= 4):       " + str(round(p_high * 100, 2)) + "%")
print("Медіана:                     " + str(median))
print("=" * 50)