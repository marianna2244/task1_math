# Задача 1. Аналітика помилок у логах

total = 500

db_only = 85
net_only = 60
db_and_net = 35

db_total = db_only + db_and_net
net_total = net_only + db_and_net

print("=" * 50)
print("АНАЛІТИКА ПОМИЛОК У ЛОГАХ")
print("=" * 50)

print("\nВхідні дані:")
print("Всього подій:              " + str(total))
print("Тільки DB помилки:         " + str(db_only))
print("Тільки NET помилки:        " + str(net_only))
print("DB та NET одночасно:       " + str(db_and_net))
print("Всього DB помилок:         " + str(db_total))
print("Всього NET помилок:        " + str(net_total))


# --- 1. Ймовірність події DB ---

print("\n1. ЙМОВІРНІСТЬ ПОМИЛКИ DB")
print("-" * 40)
print("P(A) = кількість DB подій / всього подій")
print("P(A) = " + str(db_total) + " / " + str(total))

p_a = db_total / total

print("P(A) = " + str(round(p_a, 4)))
print("P(A) = " + str(round(p_a * 100, 2)) + "%")


# --- 2. Ймовірність DB або NET ---
# Формула включень-виключень: P(A або B) = P(A) + P(B) - P(A і B)

print("\n2. ЙМОВІРНІСТЬ DB АБО NET")
print("-" * 40)
print("Формула: P(A або B) = P(A) + P(B) - P(A і B)")
print("Без віднімання перетину ми порахували б його двічі.")
print("")

p_b = net_total / total
p_a_and_b = db_and_net / total
p_a_or_b = p_a + p_b - p_a_and_b

print("P(A)     = " + str(db_total) + " / " + str(total) + " = " + str(round(p_a, 4)))
print("P(B)     = " + str(net_total) + " / " + str(total) + " = " + str(round(p_b, 4)))
print("P(A і B) = " + str(db_and_net) + " / " + str(total) + " = " + str(round(p_a_and_b, 4)))
print("")
print("P(A або B) = " + str(round(p_a, 4)) + " + " + str(round(p_b, 4)) + " - " + str(round(p_a_and_b, 4)))
print("P(A або B) = " + str(round(p_a_or_b, 4)))
print("P(A або B) = " + str(round(p_a_or_b * 100, 2)) + "%")


# --- 3. Ймовірність DB але не NET ---
# P(A \ B) = P(A) - P(A і B)

print("\n3. ЙМОВІРНІСТЬ DB АЛЕ НЕ NET")
print("-" * 40)
print("Формула: P(A \\ B) = P(A) - P(A i B)")
print("")

p_a_not_b = p_a - p_a_and_b

print("P(A \\ B) = " + str(round(p_a, 4)) + " - " + str(round(p_a_and_b, 4)))
print("P(A \\ B) = " + str(round(p_a_not_b, 4)))
print("P(A \\ B) = " + str(round(p_a_not_b * 100, 2)) + "%")


print("\n" + "=" * 50)
print("ПІДСУМОК")
print("=" * 50)
print("P(DB):           " + str(round(p_a * 100, 2)) + "%")
print("P(DB або NET):   " + str(round(p_a_or_b * 100, 2)) + "%")
print("P(DB, але NET):  " + str(round(p_a_not_b * 100, 2)) + "%")
print("=" * 50)