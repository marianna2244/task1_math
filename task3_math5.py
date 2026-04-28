# Задача 3. Час між замовленнями в інтернет-магазині

import subprocess
import sys

try:
    from scipy.stats import expon
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.stats import expon

import math

# Параметри розподілу
lam   = 0.1   # замовлень на хвилину
scale = 1 / lam  # середній час між замовленнями = 10 хвилин

print("=" * 55)
print("ЧАС МІЖ ЗАМОВЛЕННЯМИ В ІНТЕРНЕТ-МАГАЗИНІ")
print("=" * 55)

print("\nПараметри: T ~ Exponential(lambda=0.1)")
print("lambda = " + str(lam) + "  (замовлень на хвилину)")
print("scale  = 1 / lambda = " + str(scale) + "  (хвилин між замовленнями)")


# --- 1. Математичне сподівання та стандартне відхилення ---
# E[T] = 1 / lambda = scale
# Var(T) = 1 / lambda^2
# sigma = 1 / lambda = scale

print("\n" + "=" * 55)
print("1. ЧИСЛОВІ ХАРАКТЕРИСТИКИ")
print("-" * 45)

ex    = scale
var   = 1 / lam**2
sigma = math.sqrt(var)

print("E[T] = 1 / lambda = 1 / " + str(lam))
print("E[T] = " + str(round(ex, 4)) + " хвилин")

print("")
print("Var(T) = 1 / lambda^2 = 1 / " + str(lam**2))
print("Var(T) = " + str(round(var, 4)))

print("")
print("sigma = sqrt(Var(T)) = 1 / lambda")
print("sigma = " + str(round(sigma, 4)) + " хвилин")

print("")
print("Для показникового розподілу E[T] = sigma = scale = " + str(scale))


# --- 2. Ймовірність що замовлення надійде менше ніж за 5 хвилин ---
# P(T < 5) = CDF(5)

print("\n" + "=" * 55)
print("2. ЙМОВІРНІСТЬ P(T < 5 хвилин)")
print("-" * 45)
print("Використовуємо CDF: P(T < 5) = F(5)")
print("")

p_less_5 = expon.cdf(5, scale=scale)

print("P(T < 5) = expon.cdf(5, scale=10)")
print("P(T < 5) = " + str(round(p_less_5, 6)))
print("P(T < 5) = " + str(round(p_less_5 * 100, 4)) + "%")


# --- 3. Ймовірність що чекати більше 15 хвилин ---
# P(T > 15) = 1 - CDF(15)

print("\n" + "=" * 55)
print("3. ЙМОВІРНІСТЬ P(T > 15 хвилин)")
print("-" * 45)
print("P(T > 15) = 1 - F(15)")
print("")

cdf_15 = expon.cdf(15, scale=scale)
p_more_15 = 1 - cdf_15

print("F(15) = expon.cdf(15, scale=10) = " + str(round(cdf_15, 6)))
print("P(T > 15) = 1 - " + str(round(cdf_15, 6)))
print("P(T > 15) = " + str(round(p_more_15, 6)))
print("P(T > 15) = " + str(round(p_more_15 * 100, 4)) + "%")


# --- 4. Ймовірність що замовлення надійде між 5 та 15 хвилинами ---
# P(5 < T < 15) = CDF(15) - CDF(5)

print("\n" + "=" * 55)
print("4. ЙМОВІРНІСТЬ P(5 < T < 15 хвилин)")
print("-" * 45)
print("P(5 < T < 15) = F(15) - F(5)")
print("")

cdf_5 = expon.cdf(5, scale=scale)
p_5_15 = cdf_15 - cdf_5

print("F(15) = " + str(round(cdf_15, 6)))
print("F(5)  = " + str(round(cdf_5, 6)))
print("")
print("P(5 < T < 15) = " + str(round(cdf_15, 6)) + " - " + str(round(cdf_5, 6)))
print("P(5 < T < 15) = " + str(round(p_5_15, 6)))
print("P(5 < T < 15) = " + str(round(p_5_15 * 100, 4)) + "%")


# --- 5. Медіана ---
# Медіана = PPF(0.5) - час за який з ймовірністю 50% надійде замовлення

print("\n" + "=" * 55)
print("5. МЕДІАННИЙ ЧАС ОЧІКУВАННЯ")
print("-" * 45)
print("Медіана = PPF(0.5) - обернена функція CDF")
print("PPF(0.5) дає час за який P(T <= t) = 0.5")
print("")

median = expon.ppf(0.5, scale=scale)

print("Медіана = expon.ppf(0.5, scale=10)")
print("Медіана = " + str(round(median, 4)) + " хвилин")
print("")
print("Перевірка: CDF(медіана) = " + str(round(expon.cdf(median, scale=scale), 4)))


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("E[T]:            " + str(round(ex, 4)) + " хвилин")
print("sigma:           " + str(round(sigma, 4)) + " хвилин")
print("P(T < 5):        " + str(round(p_less_5 * 100, 4)) + "%")
print("P(T > 15):       " + str(round(p_more_15 * 100, 4)) + "%")
print("P(5 < T < 15):   " + str(round(p_5_15 * 100, 4)) + "%")
print("Медіана:         " + str(round(median, 4)) + " хвилин")
print("=" * 55)