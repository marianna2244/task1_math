# Задача 2. Контроль якості батарей

import math

total = 12
good = 8
defective = 4
pick = 3

print("=" * 55)
print("КОНТРОЛЬ ЯКОСТІ БАТАРЕЙ")
print("=" * 55)

print("\nВхідні дані:")
print("Всього батарей:    " + str(total))
print("Справних:          " + str(good))
print("Дефектних:         " + str(defective))
print("Вибирають:         " + str(pick))


# --- 1. Всі 3 справні через правило множення ---

print("\n1. ВСІ 3 СПРАВНІ - ПРАВИЛО МНОЖЕННЯ")
print("-" * 45)
print("Витягуємо по одній без повернення.")
print("")
print("P(1-а справна)           = 8/12")
print("P(2-а справна | 1-а була справна) = 7/11")
print("P(3-я справна | перші дві справні) = 6/10")
print("")

p1 = 8 / 12
p2 = 7 / 11
p3 = 6 / 10

p_all_good_mult = p1 * p2 * p3

print("P(всі 3 справні) = 8/12 * 7/11 * 6/10")
print("P(всі 3 справні) = " + str(round(p1, 4)) + " * " + str(round(p2, 4)) + " * " + str(round(p3, 4)))
print("P(всі 3 справні) = " + str(round(p_all_good_mult, 4)))
print("P(всі 3 справні) = " + str(round(p_all_good_mult * 100, 2)) + "%")


# --- 2. Всі 3 справні через комбінаторику ---
# C(8,3) - способів вибрати 3 справні з 8
# C(12,3) - способів вибрати будь-які 3 з 12

print("\n2. ВСІ 3 СПРАВНІ - КОМБІНАТОРНИЙ МЕТОД")
print("-" * 45)
print("C(8,3) = кількість способів вибрати 3 справні з 8")
print("C(12,3) = кількість способів вибрати будь-які 3 з 12")
print("")

c_8_3  = math.comb(8, 3)
c_12_3 = math.comb(12, 3)

p_all_good_comb = c_8_3 / c_12_3

print("C(8,3)  = " + str(c_8_3))
print("C(12,3) = " + str(c_12_3))
print("")
print("P(всі 3 справні) = C(8,3) / C(12,3)")
print("P(всі 3 справні) = " + str(c_8_3) + " / " + str(c_12_3))
print("P(всі 3 справні) = " + str(round(p_all_good_comb, 4)))
print("P(всі 3 справні) = " + str(round(p_all_good_comb * 100, 2)) + "%")
print("")

diff_1_2 = abs(p_all_good_mult - p_all_good_comb)
print("Різниця між методами: " + str(round(diff_1_2, 8)))
print("Результати збігаються.")


# --- 3. Рівно 2 справні ---

print("\n3. РІВНО 2 СПРАВНІ")
print("-" * 45)

# Спосіб 1 - правило множення
# Можливі порядки: СCД, СДС, ДСС (С=справна, Д=дефектна)
print("Спосіб 1 - правило множення")
print("")
print("Можливі порядки вибору (С=справна, Д=дефектна):")
print("")

# СCД - справна, справна, дефектна
p_SSD = (8/12) * (7/11) * (4/10)
print("Порядок С-С-Д: 8/12 * 7/11 * 4/10 = " + str(round(p_SSD, 4)))

# СДС - справна, дефектна, справна
p_SDS = (8/12) * (4/11) * (7/10)
print("Порядок С-Д-С: 8/12 * 4/11 * 7/10 = " + str(round(p_SDS, 4)))

# ДСС - дефектна, справна, справна
p_DSS = (4/12) * (8/11) * (7/10)
print("Порядок Д-С-С: 4/12 * 8/11 * 7/10 = " + str(round(p_DSS, 4)))

p_exactly_2_mult = p_SSD + p_SDS + p_DSS

print("")
print("P(рівно 2 справні) = " + str(round(p_SSD, 4)) + " + " + str(round(p_SDS, 4)) + " + " + str(round(p_DSS, 4)))
print("P(рівно 2 справні) = " + str(round(p_exactly_2_mult, 4)))
print("P(рівно 2 справні) = " + str(round(p_exactly_2_mult * 100, 2)) + "%")

# Спосіб 2 - комбінаторика
# C(8,2) - вибрати 2 справні з 8
# C(4,1) - вибрати 1 дефектну з 4
# C(12,3) - вибрати будь-які 3 з 12
print("")
print("Спосіб 2 - комбінаторика")
print("")
print("C(8,2) = вибрати 2 справні з 8")
print("C(4,1) = вибрати 1 дефектну з 4")
print("C(12,3) = вибрати будь-які 3 з 12")
print("")

c_8_2 = math.comb(8, 2)
c_4_1 = math.comb(4, 1)

p_exactly_2_comb = (c_8_2 * c_4_1) / c_12_3

print("C(8,2)  = " + str(c_8_2))
print("C(4,1)  = " + str(c_4_1))
print("C(12,3) = " + str(c_12_3))
print("")
print("P(рівно 2 справні) = C(8,2) * C(4,1) / C(12,3)")
print("P(рівно 2 справні) = " + str(c_8_2) + " * " + str(c_4_1) + " / " + str(c_12_3))
print("P(рівно 2 справні) = " + str(round(p_exactly_2_comb, 4)))
print("P(рівно 2 справні) = " + str(round(p_exactly_2_comb * 100, 2)) + "%")

diff_3 = abs(p_exactly_2_mult - p_exactly_2_comb)
print("")
print("Різниця між методами: " + str(round(diff_3, 8)))
print("Результати збігаються.")


print("\n" + "=" * 55)
print("ПІДСУМОК")
print("=" * 55)
print("P(всі 3 справні):    " + str(round(p_all_good_comb * 100, 2)) + "%")
print("P(рівно 2 справні):  " + str(round(p_exactly_2_comb * 100, 2)) + "%")
print("=" * 55)