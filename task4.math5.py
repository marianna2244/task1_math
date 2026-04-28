# Задача 4. Перевірка середнього балу студентів

import subprocess
import sys

try:
    from scipy.stats import t
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    from scipy.stats import t

import math

# Вхідні дані
x_bar = 76.8   # вибіркове середнє
mu_0  = 72.0   # середнє минулого року
s     = 14.2   # вибіркове стандартне відхилення
n     = 35     # розмір вибірки
alpha = 0.05   # рівень значущості
df    = n - 1  # ступені свободи

print("=" * 55)
print("ПЕРЕВІРКА СЕРЕДНЬОГО БАЛУ СТУДЕНТІВ")
print("=" * 55)

print("\nВхідні дані:")
print("Середнє минулого року  mu_0 = " + str(mu_0))
print("Вибіркове середнє     x_bar = " + str(x_bar))
print("Стандартне відхилення     s = " + str(s))
print("Розмір вибірки            n = " + str(n))
print("Рівень значущості     alpha = " + str(alpha))
print("Ступені свободи          df = n - 1 = " + str(df))


# --- 1. Формулювання гіпотез ---

print("\n" + "=" * 55)
print("1. ФОРМУЛЮВАННЯ ГІПОТЕЗ")
print("-" * 45)
print("H0: mu = 72  (нова методика не вплинула на результати)")
print("H1: mu != 72 (нова методика вплинула на результати)")
print("")
print("Двосторонній тест, бо нас цікавить будь-яка зміна,")
print("як покращення так і погіршення.")


# --- 2. Стандартна похибка ---
# SE = s / sqrt(n)

print("\n" + "=" * 55)
print("2. СТАНДАРТНА ПОХИБКА")
print("-" * 45)
print("SE = s / sqrt(n)")
print("")

se = s / math.sqrt(n)

print("SE = " + str(s) + " / sqrt(" + str(n) + ")")
print("SE = " + str(s) + " / " + str(round(math.sqrt(n), 4)))
print("SE = " + str(round(se, 4)))


# --- 3. t-статистика ---
# t = (x_bar - mu_0) / SE

print("\n" + "=" * 55)
print("3. T-СТАТИСТИКА")
print("-" * 45)
print("t = (x_bar - mu_0) / SE")
print("")

t_stat = (x_bar - mu_0) / se

print("t = (" + str(x_bar) + " - " + str(mu_0) + ") / " + str(round(se, 4)))
print("t = " + str(round(x_bar - mu_0, 4)) + " / " + str(round(se, 4)))
print("t = " + str(round(t_stat, 4)))


# --- 4. p-value ---
# Двосторонній тест: p = 2 * P(T > |t|) = 2 * (1 - CDF(|t|))

print("\n" + "=" * 55)
print("4. P-VALUE (двосторонній тест)")
print("-" * 45)
print("p = 2 * (1 - CDF(|t|))")
print("")

cdf_val = t.cdf(abs(t_stat), df)
p_value = 2 * (1 - cdf_val)

print("CDF(|t|) = t.cdf(" + str(round(abs(t_stat), 4)) + ", df=" + str(df) + ")")
print("CDF(|t|) = " + str(round(cdf_val, 6)))
print("")
print("p-value = 2 * (1 - " + str(round(cdf_val, 6)) + ")")
print("p-value = 2 * " + str(round(1 - cdf_val, 6)))
print("p-value = " + str(round(p_value, 6)))


# --- 5. Довірчий інтервал 95% ---
# CI = x_bar +/- t_crit * SE
# t_crit = PPF(1 - alpha/2) для двостороннього тесту

print("\n" + "=" * 55)
print("5. ДОВІРЧИЙ ІНТЕРВАЛ 95%")
print("-" * 45)
print("CI = x_bar +/- t_crit * SE")
print("t_crit = t.ppf(1 - alpha/2, df)")
print("")

t_crit = t.ppf(1 - alpha / 2, df)

ci_lower = x_bar - t_crit * se
ci_upper = x_bar + t_crit * se

print("t_crit = t.ppf(" + str(1 - alpha / 2) + ", df=" + str(df) + ")")
print("t_crit = " + str(round(t_crit, 4)))
print("")
print("CI нижня межа = " + str(x_bar) + " - " + str(round(t_crit, 4)) + " * " + str(round(se, 4)))
print("CI нижня межа = " + str(round(ci_lower, 4)))
print("")
print("CI верхня межа = " + str(x_bar) + " + " + str(round(t_crit, 4)) + " * " + str(round(se, 4)))
print("CI верхня межа = " + str(round(ci_upper, 4)))
print("")
print("95% довірчий інтервал: [" + str(round(ci_lower, 2)) + " ; " + str(round(ci_upper, 2)) + "]")


# --- 6. Висновок ---

print("\n" + "=" * 55)
print("6. ВИСНОВОК")
print("-" * 45)
print("p-value = " + str(round(p_value, 6)))
print("alpha   = " + str(alpha))
print("")

if p_value < alpha:
    print("p-value < alpha (" + str(round(p_value, 4)) + " < " + str(alpha) + ")")
    print("")
    print("Відхиляємо H0.")
    print("Є статистично значущі підстави стверджувати,")
    print("що нова методика вплинула на результати.")
    print("Середній бал зріс з " + str(mu_0) + " до " + str(x_bar) + ".")
else:
    print("p-value >= alpha (" + str(round(p_value, 4)) + " >= " + str(alpha) + ")")
    print("")
    print("Не відхиляємо H0.")
    print("Немає достатніх підстав стверджувати,")
    print("що нова методика вплинула на результати.")

print("\nДодаткова перевірка через довірчий інтервал:")
print("mu_0 = " + str(mu_0) + " входить в інтервал [" + str(round(ci_lower, 2)) + " ; " + str(round(ci_upper, 2)) + "]?")

if ci_lower <= mu_0 <= ci_upper:
    print("Так -> H0 не відхиляється.")
else:
    print("Ні -> H0 відхиляється. Результат збігається з p-value.")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("SE:              " + str(round(se, 4)))
print("t-статистика:    " + str(round(t_stat, 4)))
print("p-value:         " + str(round(p_value, 6)))
print("t_crit:          " + str(round(t_crit, 4)))
print("95% CI:          [" + str(round(ci_lower, 2)) + " ; " + str(round(ci_upper, 2)) + "]")
print("=" * 55)