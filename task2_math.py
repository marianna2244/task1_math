# Задача 2. Пошук схожих фільмів за косинусною подібністю

import subprocess
import sys

try:
    import numpy as np
except ImportError:
    print("Встановлення numpy...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np

# Вектор профілю користувача та вектори фільмів
u = np.array([8, 2, 5])

films = {
    "Фільм A (Action Movie)": np.array([9, 1, 2]),
    "Фільм B (Comedy Movie)": np.array([1, 9, 8]),
    "Фільм C (Drama Movie)":  np.array([7, 2, 6]),
}


def cosine_similarity(u, v):
    """Косинусна подібність між двома векторами."""
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    return dot_product / (norm_u * norm_v)


def main():
    print("=" * 50)
    print("       ПОШУК СХОЖИХ ФІЛЬМІВ")
    print("=" * 50)

    norm_u = np.linalg.norm(u)
    print(f"\nВектор користувача u = {u}")
    print(f"Норма вектора ‖u‖ = {norm_u:.4f}")

    print("\nКоефіцієнти косинусної подібності:")
    print("-" * 40)

    scores = {}
    for name, v in films.items():
        score = cosine_similarity(u, v)
        scores[name] = score
        print(f"{name}: {score:.4f}")

    best_film = max(scores, key=scores.get)
    print("-" * 40)
    print(f"\n✅ Найкращий фільм: {best_film}")
    print(f"   Схожість: {scores[best_film]:.4f}")
    print("=" * 50)


if __name__ == "__main__":
    main()