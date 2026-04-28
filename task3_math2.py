# Задача 3. Формування "Команди мрії"

import math


def main():
    print("=" * 55)
    print("       ФОРМУВАННЯ «КОМАНДИ МРІЇ»")
    print("=" * 55)

    # Вхідні дані
    backend_total   = 8
    frontend_total  = 6
    design_total    = 4

    backend_needed  = 2
    frontend_needed = 2
    design_needed   = 1

    print("\n📋 Пул кандидатів:")
    print(f"   Back-end розробників : {backend_total} осіб, обираємо {backend_needed}")
    print(f"   Front-end розробників: {frontend_total} осіб, обираємо {frontend_needed}")
    print(f"   UI/UX дизайнерів     : {design_total} особи, обираємо {design_needed}")

    # 1. Сполучення для Back-end: C(8, 2)
    backend_ways = math.comb(backend_total, backend_needed)
    print(f"\n1. Способів обрати {backend_needed} back-end розробники з {backend_total}:")
    print(f"   C({backend_total}, {backend_needed}) = {backend_total}! / ({backend_needed}! × {backend_total - backend_needed}!) = {backend_ways}")

    # 2. Сполучення для Front-end: C(6, 2)
    frontend_ways = math.comb(frontend_total, frontend_needed)
    print(f"\n2. Способів обрати {frontend_needed} front-end розробники з {frontend_total}:")
    print(f"   C({frontend_total}, {frontend_needed}) = {frontend_total}! / ({frontend_needed}! × {frontend_total - frontend_needed}!) = {frontend_ways}")

    # 3. Сполучення для дизайнерів: C(4, 1)
    design_ways = math.comb(design_total, design_needed)
    print(f"\n3. Способів обрати {design_needed} дизайнера з {design_total}:")
    print(f"   C({design_total}, {design_needed}) = {design_total}! / ({design_needed}! × {design_total - design_needed}!) = {design_ways}")

    # 4. Правило множення
    total = backend_ways * frontend_ways * design_ways
    print(f"\n4. Загальна кількість унікальних складів команди:")
    print(f"   C(8,2) × C(6,2) × C(4,1) = {backend_ways} × {frontend_ways} × {design_ways} = {total}")

    print("\n" + "=" * 55)
    print(f"✅ Команду мрії можна сформувати {total} різними способами.")
    print("=" * 55)


if __name__ == "__main__":
    main()