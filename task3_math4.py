# Задача 3. Надійність розподіленої системи

# Ймовірності відмови кожного вузла
p_fail_a = 0.02
p_fail_b = 0.05
p_fail_c = 0.03
p_fail_d = 0.04

# Ймовірності що кожен вузол ПРАЦЮЄ
p_work_a = 1 - p_fail_a
p_work_b = 1 - p_fail_b
p_work_c = 1 - p_fail_c
p_work_d = 1 - p_fail_d

print("=" * 55)
print("НАДІЙНІСТЬ РОЗПОДІЛЕНОЇ СИСТЕМИ")
print("=" * 55)

print("\nВхідні дані:")
print("Вузол A - ймовірність відмови: " + str(p_fail_a))
print("Вузол B - ймовірність відмови: " + str(p_fail_b))
print("Вузол C - ймовірність відмови: " + str(p_fail_c))
print("Вузол D - ймовірність відмови: " + str(p_fail_d))
print("")
print("Ймовірності що вузли ПРАЦЮЮТЬ:")
print("Вузол A: 1 - " + str(p_fail_a) + " = " + str(p_work_a))
print("Вузол B: 1 - " + str(p_fail_b) + " = " + str(p_work_b))
print("Вузол C: 1 - " + str(p_fail_c) + " = " + str(p_work_c))
print("Вузол D: 1 - " + str(p_fail_d) + " = " + str(p_work_d))


# --- 1. Всі 4 вузли працюють ---
# Вузли незалежні, тому множимо ймовірності

print("\n1. ВСІ 4 ВУЗЛИ ПРАЦЮЮТЬ")
print("-" * 45)
print("Вузли незалежні, тому:")
print("P(всі працюють) = P(A) * P(B) * P(C) * P(D)")
print("")
print("P(всі працюють) = " + str(p_work_a) + " * " + str(p_work_b) + " * " + str(p_work_c) + " * " + str(p_work_d))

p_all_work = p_work_a * p_work_b * p_work_c * p_work_d

print("P(всі працюють) = " + str(round(p_all_work, 6)))
print("P(всі працюють) = " + str(round(p_all_work * 100, 4)) + "%")


# --- 2. Хоча б один відмовить ---
# Протилежна подія до "всі працюють"

print("\n2. ХОЧА Б ОДИН ВІДМОВИТЬ")
print("-" * 45)
print("Використовуємо протилежну подію:")
print("P(хоча б один відмовить) = 1 - P(всі працюють)")
print("")

p_at_least_one_fail = 1 - p_all_work

print("P(хоча б один відмовить) = 1 - " + str(round(p_all_work, 6)))
print("P(хоча б один відмовить) = " + str(round(p_at_least_one_fail, 6)))
print("P(хоча б один відмовить) = " + str(round(p_at_least_one_fail * 100, 4)) + "%")


# --- 3. Рівно два вузли відмовлять ---
# Перебираємо всі 6 пар вузлів
# Для кожної пари: два вузли відмовляють, два інші працюють

print("\n3. РІВНО ДВА ВУЗЛИ ВІДМОВЛЯТЬ")
print("-" * 45)
print("Перебираємо всі 6 можливих пар вузлів.")
print("Для кожної пари: ці два відмовляють, решта два працюють.")
print("")

# Пара AB - відмовили A і B, працюють C і D
p_ab = p_fail_a * p_fail_b * p_work_c * p_work_d
print("Пара A і B відмовили:")
print("  " + str(p_fail_a) + " * " + str(p_fail_b) + " * " + str(p_work_c) + " * " + str(p_work_d) + " = " + str(round(p_ab, 6)))

# Пара AC - відмовили A і C, працюють B і D
p_ac = p_fail_a * p_work_b * p_fail_c * p_work_d
print("Пара A і C відмовили:")
print("  " + str(p_fail_a) + " * " + str(p_work_b) + " * " + str(p_fail_c) + " * " + str(p_work_d) + " = " + str(round(p_ac, 6)))

# Пара AD - відмовили A і D, працюють B і C
p_ad = p_fail_a * p_work_b * p_work_c * p_fail_d
print("Пара A і D відмовили:")
print("  " + str(p_fail_a) + " * " + str(p_work_b) + " * " + str(p_work_c) + " * " + str(p_fail_d) + " = " + str(round(p_ad, 6)))

# Пара BC - відмовили B і C, працюють A і D
p_bc = p_work_a * p_fail_b * p_fail_c * p_work_d
print("Пара B і C відмовили:")
print("  " + str(p_work_a) + " * " + str(p_fail_b) + " * " + str(p_fail_c) + " * " + str(p_work_d) + " = " + str(round(p_bc, 6)))

# Пара BD - відмовили B і D, працюють A і C
p_bd = p_work_a * p_fail_b * p_work_c * p_fail_d
print("Пара B і D відмовили:")
print("  " + str(p_work_a) + " * " + str(p_fail_b) + " * " + str(p_work_c) + " * " + str(p_fail_d) + " = " + str(round(p_bd, 6)))

# Пара CD - відмовили C і D, працюють A і B
p_cd = p_work_a * p_work_b * p_fail_c * p_fail_d
print("Пара C і D відмовили:")
print("  " + str(p_work_a) + " * " + str(p_work_b) + " * " + str(p_fail_c) + " * " + str(p_fail_d) + " = " + str(round(p_cd, 6)))

p_exactly_two = p_ab + p_ac + p_ad + p_bc + p_bd + p_cd

print("")
print("Підсумовуємо всі 6 комбінацій:")
print(str(round(p_ab, 6)) + " + " + str(round(p_ac, 6)) + " + " + str(round(p_ad, 6)) + " + " + str(round(p_bc, 6)) + " + " + str(round(p_bd, 6)) + " + " + str(round(p_cd, 6)))
print("")
print("P(рівно два відмовлять) = " + str(round(p_exactly_two, 6)))
print("P(рівно два відмовлять) = " + str(round(p_exactly_two * 100, 4)) + "%")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("P(всі працюють):         " + str(round(p_all_work * 100, 4)) + "%")
print("P(хоча б один відмовить): " + str(round(p_at_least_one_fail * 100, 4)) + "%")
print("P(рівно два відмовлять):  " + str(round(p_exactly_two * 100, 4)) + "%")
print("=" * 55)