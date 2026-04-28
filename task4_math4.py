# Задача 4. Визначення джерела трафіку

# Апріорні ймовірності джерел (звідки прийшов відвідувач)
p_h1 = 0.50  # пошукова реклама
p_h2 = 0.30  # соцмережі
p_h3 = 0.20  # email-розсилка

# Конверсія кожного джерела (ймовірність покупки)
p_a_h1 = 0.04  # купив, якщо прийшов з пошуку
p_a_h2 = 0.02  # купив, якщо прийшов з соцмереж
p_a_h3 = 0.08  # купив, якщо прийшов з email


# --- Функція для довільної кількості джерел ---

def bayes_source(prior_probs, conversion_rates):
    # Крок 1. Обчислюємо добутки P(Hi) * P(A|Hi) для кожного джерела
    products = []
    for i in range(len(prior_probs)):
        products.append(prior_probs[i] * conversion_rates[i])

    # Крок 2. Повна ймовірність покупки - сума всіх добутків
    p_total = sum(products)

    # Крок 3. Апостеріорна ймовірність кожного джерела за Баєсом
    # P(Hi|A) = P(Hi) * P(A|Hi) / P(A)
    posterior = []
    for i in range(len(prior_probs)):
        posterior.append(products[i] / p_total)

    return posterior


print("=" * 55)
print("ВИЗНАЧЕННЯ ДЖЕРЕЛА ТРАФІКУ")
print("=" * 55)

print("\nВхідні дані:")
print("Пошукова реклама: трафік = 50%, конверсія = 4%")
print("Соцмережі:        трафік = 30%, конверсія = 2%")
print("Email-розсилка:   трафік = 20%, конверсія = 8%")


# --- 1. Повна ймовірність покупки ---

print("\n1. ЗАГАЛЬНА ЙМОВІРНІСТЬ ПОКУПКИ")
print("-" * 45)
print("Формула повної ймовірності:")
print("P(A) = P(H1)*P(A|H1) + P(H2)*P(A|H2) + P(H3)*P(A|H3)")
print("")

part1 = p_h1 * p_a_h1
part2 = p_h2 * p_a_h2
part3 = p_h3 * p_a_h3

print("P(H1)*P(A|H1) = " + str(p_h1) + " * " + str(p_a_h1) + " = " + str(part1))
print("P(H2)*P(A|H2) = " + str(p_h2) + " * " + str(p_a_h2) + " = " + str(part2))
print("P(H3)*P(A|H3) = " + str(p_h3) + " * " + str(p_a_h3) + " = " + str(part3))
print("")

p_a_total = part1 + part2 + part3

print("P(A) = " + str(part1) + " + " + str(part2) + " + " + str(part3))
print("P(A) = " + str(round(p_a_total, 4)))
print("P(A) = " + str(round(p_a_total * 100, 2)) + "%")


# --- 2. Ймовірність що покупець прийшов з email ---

print("\n2. ЙМОВІРНІСТЬ ЩО ПОКУПЕЦЬ З EMAIL (теорема Баєса)")
print("-" * 45)
print("Формула Баєса:")
print("P(H3|A) = P(H3) * P(A|H3) / P(A)")
print("")

p_h3_a = (p_h3 * p_a_h3) / p_a_total

print("P(H3|A) = " + str(p_h3) + " * " + str(p_a_h3) + " / " + str(round(p_a_total, 4)))
print("P(H3|A) = " + str(part3) + " / " + str(round(p_a_total, 4)))
print("P(H3|A) = " + str(round(p_h3_a, 4)))
print("P(H3|A) = " + str(round(p_h3_a * 100, 2)) + "%")


# --- 3. Функція для довільної кількості джерел ---

print("\n3. ПЕРЕВІРКА ФУНКЦІЇ bayes_source")
print("-" * 45)

prior_probs      = [0.50, 0.30, 0.20]
conversion_rates = [0.04, 0.02, 0.08]
source_names     = ["Пошукова реклама", "Соцмережі", "Email-розсилка"]

posterior = bayes_source(prior_probs, conversion_rates)

print("Апостеріорні ймовірності кожного джерела")
print("(якщо відомо що покупка відбулась):")
print("")

for i in range(len(source_names)):
    print(source_names[i] + ": " + str(round(posterior[i], 4)) + "  (" + str(round(posterior[i] * 100, 2)) + "%)")

print("")
print("Сума всіх апостеріорних ймовірностей: " + str(round(sum(posterior), 6)))
print("(має дорівнювати 1.0 - перевірка правильності)")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("Загальна ймовірність покупки:          " + str(round(p_a_total * 100, 2)) + "%")
print("Якщо покупка - ймовірність що з email: " + str(round(p_h3_a * 100, 2)) + "%")
print("")
print("Email-розсилка має найвищу апостеріорну ймовірність,")
print("хоча дає лише 20% трафіку - через найвищу конверсію 8%.")
print("=" * 55)