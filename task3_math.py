# Задача 3. Аналіз виробництва FPV-дронів

import subprocess
import sys

try:
    import numpy as np
except ImportError:
    print("Встановлення numpy...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# Матриця коефіцієнтів A (рядки — деталі, стовпці — типи дронів)
A = np.array([
    [4, 4, 6],  # мотори
    [1, 1, 2],  # контролери
    [1, 2, 4],  # акумулятори
])

# Вектор витрат b
b = np.array([460, 130, 240])


def main():
    print("=" * 50)
    print("     АНАЛІЗ ВИРОБНИЦТВА FPV-ДРОНІВ")
    print("=" * 50)

    # Матриця та вектор
    print("\nМатриця коефіцієнтів A:")
    print(A)
    print(f"\nВектор витрат b: {b}")

    # Перевірка визначника
    det = np.linalg.det(A)
    print(f"\nВизначник матриці A: {det:.4f}")

    if abs(det) < 1e-9:
        print("❌ Визначник = 0. Система не має єдиного розв'язку.")
        return

    print("✅ Визначник ≠ 0. Система має єдиний розв'язок.")

    # Розв'язання системи
    x = np.linalg.solve(A, b)
    print("\nКількість зібраних дронів:")
    print("-" * 35)
    print(f"  Розвідник  (x1): {round(x[0])} шт.")
    print(f"  Камікадзе  (x2): {round(x[1])} шт.")
    print(f"  Вантажний  (x3): {round(x[2])} шт.")

    # Перевірка: A @ x має дорівнювати b
    check = A @ x
    print("\nПеревірка A·x = b:")
    print("-" * 35)
    print(f"  A·x = {np.round(check).astype(int)}")
    print(f"  b   = {b}")

    if np.allclose(check, b):
        print("✅ Перевірка пройдена. Результат збігається з b.")
    else:
        print("❌ Помилка. Результат не збігається з b.")

    print("=" * 50)


if __name__ == "__main__":
    main()