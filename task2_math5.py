# Задача 2. Аналіз доставки замовлень

import subprocess
import sys

try:
    from scipy.stats import binom
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.stats import binom

import math

# Параметри біноміального розподілу
n = 50    # кількість замовлень
p = 0.88  # ймовірність вчасної доставки

print("=" * 55)
print("АНАЛІЗ ДОСТАВКИ ЗАМОВЛЕНЬ")
print("=" * 55)

print("\nПараметри розподілу: X ~ Binomial(n=50, p=0.88)")
print("n = " + str(n) + "  (замовлень відправлено)")
print("p = " + str(p) + "  (ймовірність вчасної доставки)")


# --- 1. Математичне сподівання та стандартне відхилення ---
# E[X] = n * p
# Var(X) = n * p * (1 - p)
# sigma = sqrt(Var(X))

print("\n" + "=" * 55)
print("1. ЧИСЛОВІ ХАРАКТЕРИСТИКИ")
print("-" * 45)

ex    = n * p
var   = n * p * (1 - p)
sigma = math.sqrt(var)

print("E[X] = n * p")
print("E[X] = " + str(n) + " * " + str(p))
print("E[X] = " + str(round(ex, 4)))

print("")
print("Var(X) = n * p * (1 - p)")
print("Var(X) = " + str(n) + " * " + str(p) + " * " + str(round(1 - p, 2)))
print("Var(X) = " + str(round(var, 4)))

print("")
print("sigma = sqrt(Var(X))")
print("sigma = sqrt(" + str(round(var, 4)) + ")")
print("sigma = " + str(round(sigma, 4)))


# --- 2. Ймовірність що всі 50 доставлять вчасно ---
# P(X = 50) - використовуємо PMF

print("\n" + "=" * 55)
print("2. ЙМОВІРНІСТЬ P(X = 50) - ВСІ ВЧАСНО")
print("-" * 45)
print("Використовуємо PMF: P(X = k) = binom.pmf(k, n, p)")
print("")

p_50 = binom.pmf(50, n, p)

print("P(X = 50) = binom.pmf(50, 50, 0.88)")
print("P(X = 50) = " + str(round(p_50, 6)))
print("P(X = 50) = " + str(round(p_50 * 100, 4)) + "%")


# --- 3. Ймовірність що рівно 45 доставлять вчасно ---
# P(X = 45) - використовуємо PMF

print("\n" + "=" * 55)
print("3. ЙМОВІРНІСТЬ P(X = 45) - РІВНО 45 ВЧАСНО")
print("-" * 45)

p_45 = binom.pmf(45, n, p)

print("P(X = 45) = binom.pmf(45, 50, 0.88)")
print("P(X = 45) = " + str(round(p_45, 6)))
print("P(X = 45) = " + str(round(p_45 * 100, 4)) + "%")


# --- 4. Ймовірність від 42 до 46 вчасно ---
# P(42 <= X <= 46) = CDF(46) - CDF(41)

print("\n" + "=" * 55)
print("4. ЙМОВІРНІСТЬ P(42 <= X <= 46)")
print("-" * 45)
print("Використовуємо CDF: P(42 <= X <= 46) = F(46) - F(41)")
print("")

cdf_46 = binom.cdf(46, n, p)
cdf_41 = binom.cdf(41, n, p)
p_42_46 = cdf_46 - cdf_41

print("F(46) = binom.cdf(46, 50, 0.88) = " + str(round(cdf_46, 6)))
print("F(41) = binom.cdf(41, 50, 0.88) = " + str(round(cdf_41, 6)))
print("")
print("P(42 <= X <= 46) = " + str(round(cdf_46, 6)) + " - " + str(round(cdf_41, 6)))
print("P(42 <= X <= 46) = " + str(round(p_42_46, 6)))
print("P(42 <= X <= 46) = " + str(round(p_42_46 * 100, 4)) + "%")


# --- 5. Ймовірність що більше 5 запізняться ---
# Якщо більше 5 запізняться, то вчасно доставлять менше 45
# P(більше 5 запізнились) = P(X < 45) = P(X <= 44) = CDF(44)

print("\n" + "=" * 55)
print("5. ЙМОВІРНІСТЬ ЩО БІЛЬШЕ 5 ЗАПІЗНЯТЬСЯ")
print("-" * 45)
print("Якщо запізнились більше 5, то вчасно менше 45.")
print("P(запізнилось > 5) = P(X < 45) = P(X <= 44) = F(44)")
print("")

p_late_5 = binom.cdf(44, n, p)

print("F(44) = binom.cdf(44, 50, 0.88) = " + str(round(p_late_5, 6)))
print("P(більше 5 запізняться) = " + str(round(p_late_5, 6)))
print("P(більше 5 запізняться) = " + str(round(p_late_5 * 100, 4)) + "%")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("E[X]:                    " + str(round(ex, 4)))
print("sigma:                   " + str(round(sigma, 4)))
print("P(всі 50 вчасно):        " + str(round(p_50 * 100, 4)) + "%")
print("P(рівно 45 вчасно):      " + str(round(p_45 * 100, 4)) + "%")
print("P(від 42 до 46 вчасно):  " + str(round(p_42_46 * 100, 4)) + "%")
print("P(більше 5 запізняться): " + str(round(p_late_5 * 100, 4)) + "%")
print("=" * 55)