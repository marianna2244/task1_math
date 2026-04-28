# Задача 1. Робота з зображеннями як з матрицями

M = [
    [100, 150, 200],
    [ 50, 100, 150],
    [  0,  50, 100]
]

E = [
    [20, 30, 40],
    [10, 20, 30],
    [ 5, 10, 15]
]


def print_matrix(name, matrix):
    print(f"\n{name}:")
    for row in matrix:
        print([round(val, 1) for val in row])


def scale_matrix(matrix, lam):
    """Зміна контрасту — множення кожного елемента на скаляр."""
    return [[elem * lam for elem in row] for row in matrix]


def add_scalar(matrix, c):
    """Корекція яскравості — додавання скаляра до кожного елемента."""
    return [[elem + c for elem in row] for row in matrix]


def blend(m1, m2, alpha=0.8, beta=0.2):
    """Змішування — лінійна комбінація двох матриць."""
    rows = len(m1)
    cols = len(m1[0])
    return [
        [alpha * m1[i][j] + beta * m2[i][j] for j in range(cols)]
        for i in range(rows)
    ]


def main():
    print_matrix("Оригінал M", M)
    print_matrix("Ефект E", E)

    contrast = scale_matrix(M, 0.5)
    print_matrix("1. Зміна контрасту (M × 0.5)", contrast)

    brightness = add_scalar(M, 25)
    print_matrix("2. Корекція яскравості (M + 25)", brightness)

    blended = blend(M, E)
    print_matrix("3. Змішування (0.8·M + 0.2·E)", blended)


if __name__ == "__main__":
    main()