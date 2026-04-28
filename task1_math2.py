# Задача 1. Аналітика музичного сервісу

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import matplotlib.pyplot as plt
except ImportError:
    install("matplotlib")
    import matplotlib.pyplot as plt

try:
    from matplotlib_venn import venn3
except ImportError:
    install("matplotlib-venn")
    from matplotlib_venn import venn3

# Вхідні дані
rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans  = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}


def main():
    print("=" * 55)
    print("       АНАЛІТИКА МУЗИЧНОГО СЕРВІСУ")
    print("=" * 55)

    # 1. Загальне охоплення — об'єднання всіх множин
    all_users = rock_fans | pop_fans | jazz_fans
    print(f"\n1. Загальне охоплення (унікальних користувачів):")
    print(f"   {sorted(all_users)}")
    print(f"   Кількість: {len(all_users)}")

    # 2. Меломани — перетин усіх трьох множин
    all_genres = rock_fans & pop_fans & jazz_fans
    print(f"\n2. Слухали всі три жанри (меломани):")
    print(f"   ID: {sorted(all_genres)}")
    print(f"   Кількість: {len(all_genres)}")

    # 3. Чисті рокери — рок, але НЕ поп і НЕ джаз
    pure_rock = rock_fans - pop_fans - jazz_fans
    print(f"\n3. Чисті рокери (рок, але не поп і не джаз):")
    print(f"   ID: {sorted(pure_rock)}")
    print(f"   Кількість: {len(pure_rock)}")

    # 4. Рівно два жанри — є в двох, але не в усіх трьох
    rock_and_pop  = (rock_fans & pop_fans)  - jazz_fans
    rock_and_jazz = (rock_fans & jazz_fans) - pop_fans
    pop_and_jazz  = (pop_fans  & jazz_fans) - rock_fans
    exactly_two = rock_and_pop | rock_and_jazz | pop_and_jazz

    print(f"\n4. Слухали рівно два жанри:")
    print(f"   Рок + Поп:  {sorted(rock_and_pop)}")
    print(f"   Рок + Джаз: {sorted(rock_and_jazz)}")
    print(f"   Поп + Джаз: {sorted(pop_and_jazz)}")
    print(f"   Всього: {sorted(exactly_two)}")
    print(f"   Кількість: {len(exactly_two)}")

    # 5. Діаграма Венна
    plt.figure(figsize=(8, 6))
    venn3(
        subsets=[rock_fans, pop_fans, jazz_fans],
        set_labels=("Рок", "Поп", "Джаз")
    )
    plt.title("Діаграма Венна: перетин аудиторій жанрів", fontsize=14)
    plt.tight_layout()
    plt.savefig("venn_diagram.png", dpi=150)
    plt.show()
    print("\n5. Діаграму Венна збережено у файл: venn_diagram.png")
    print("=" * 55)


if __name__ == "__main__":
    main()