# Задача 4. Прогноз тренду навантаження CPU

import subprocess
import sys

try:
    import numpy as np
except ImportError:
    print("Встановлення numpy...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# Вхідні дані
t = np.array([1, 2, 3, 4, 5])
y = np.array([22, 28, 37, 45, 53])


def main():
    print("=" * 50)
    print("      ПРОГНОЗ ТРЕНДУ НАВАНТАЖЕННЯ CPU")
    print("=" * 50)

    print(f"\nЧас t:          {t}")
    print(f"Навантаження y: {y}")

    # --- 1. Формування матриці A ---
    # Стовпець t + стовпець одиниць (для вільного члена b)
    A = np.column_stack([t, np.ones(len(t))])
    print("\nМатриця A:")
    print(A)

    # --- 2. МНК через np.linalg.lstsq ---
    result = np.linalg.lstsq(A, y, rcond=None)
    k, b = result[0]
    print(f"\n--- Метод lstsq ---")
    print(f"Нахил     k = {k:.4f}")
    print(f"Зсув      b = {b:.4f}")
    print(f"Рівняння тренду: y = {k:.4f}·t + ({b:.4f})")

    # --- 3. Прогноз на 6-ту годину ---
    t6 = 6
    y6 = k * t6 + b
    print(f"\nПрогноз на {t6}-ту годину: {y6:.2f}%")

    # --- Бонус: нормальне рівняння вручну ---
    print("\n--- Бонус: нормальне рівняння (AᵀA·x = Aᵀy) ---")
    ATA = A.T @ A
    ATy = A.T @ y
    x_manual = np.linalg.solve(ATA, ATy)
    k_m, b_m = x_manual
    print(f"Нахил     k = {k_m:.4f}")
    print(f"Зсув      b = {b_m:.4f}")
    print(f"Рівняння тренду: y = {k_m:.4f}·t + ({b_m:.4f})")

    y6_m = k_m * t6 + b_m
    print(f"Прогноз на {t6}-ту годину: {y6_m:.2f}%")

    # --- Порівняння ---
    print("\n--- Порівняння результатів ---")
    print("-" * 35)
    if np.allclose([k, b], [k_m, b_m]):
        print("✅ Результати lstsq та нормального рівняння збігаються.")
    else:
        print("❌ Результати відрізняються.")
    print("=" * 50)


if __name__ == "__main__":
    main()