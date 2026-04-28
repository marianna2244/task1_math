# Задача 2. Конфігуратор доступу до системи (RBAC)

import itertools


def check_access(is_employee, is_verified, is_premium, is_admin, is_banned):
    """Перевірка рівнів доступу користувача."""
    base    = is_employee and is_verified and not is_banned
    premium = (is_employee or is_premium) and is_verified and not is_banned
    admin   = is_admin and is_verified and not is_banned
    secret  = (is_admin or (is_employee and is_premium)) and is_verified and not is_banned

    return {
        "Base":    base,
        "Premium": premium,
        "Admin":   admin,
        "Secret":  secret,
    }


def main():
    print("=" * 65)
    print("       КОНФІГУРАТОР ДОСТУПУ ДО СИСТЕМИ (RBAC)")
    print("=" * 65)

    # Заголовок таблиці
    header = f"{'Emp':<6}{'Ver':<6}{'Prem':<6}{'Adm':<6}{'Ban':<6}| {'Base':<6}{'Prem':<6}{'Adm':<6}{'Secr':<6}"
    print(header)
    print("-" * 65)

    all_combinations = list(itertools.product([True, False], repeat=5))
    results = []

    for combo in all_combinations:
        emp, ver, prem, adm, ban = combo
        access = check_access(emp, ver, prem, adm, ban)

        row = (
            f"{int(emp):<6}{int(ver):<6}{int(prem):<6}{int(adm):<6}{int(ban):<6}| "
            f"{int(access['Base']):<6}{int(access['Premium']):<6}"
            f"{int(access['Admin']):<6}{int(access['Secret']):<6}"
        )
        print(row)
        results.append((combo, access))

    print("=" * 65)

    # --- Аналіз ---
    print("\n📊 АНАЛІЗ РЕЗУЛЬТАТІВ")
    print("-" * 65)

    # Повний доступ (всі 4 секції)
    full_access = [
        r for r in results
        if all(r[1].values())
    ]
    print(f"\n1. Кількість комбінацій з повним доступом (всі 4 секції): {len(full_access)}")
    if full_access:
        print("   Комбінації (Emp, Ver, Prem, Adm, Ban):")
        for combo, _ in full_access:
            print(f"   {tuple(int(x) for x in combo)}")

    # Premium без Base
    prem_no_base = [
        r for r in results
        if r[1]["Premium"] and not r[1]["Base"]
    ]
    print(f"\n2. Комбінації де є Premium, але немає Base: {len(prem_no_base)}")
    if prem_no_base:
        print("   (Emp, Ver, Prem, Adm, Ban):")
        for combo, access in prem_no_base:
            print(f"   {tuple(int(x) for x in combo)}")
        print(
            "\n   💡 Пояснення: Premium доступ отримує той, хто має преміум-підписку\n"
            "   (is_premium=True), навіть якщо не є співробітником.\n"
            "   Base доступ вимагає обов'язково is_employee=True.\n"
            "   Тому не-співробітник з преміумом має Premium, але не має Base."
        )

    print("=" * 65)


if __name__ == "__main__":
    main()