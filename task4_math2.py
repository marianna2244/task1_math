# Задача 4. Аналіз соціальної мережі компанії

# Список суміжності - словник де ключ це співробітник, значення - список контактів
adjacency_list = {
    "Анна":   ["Богдан", "Віктор", "Ганна"],
    "Богдан": ["Анна", "Віктор", "Дмитро"],
    "Віктор": ["Анна", "Богдан", "Ганна", "Дмитро"],
    "Ганна":  ["Анна", "Віктор", "Євген"],
    "Дмитро": ["Богдан", "Віктор", "Євген"],
    "Євген":  ["Ганна", "Дмитро"],
}

employees = list(adjacency_list.keys())


# --- Матриця суміжності ---
def build_adjacency_matrix():
    n = len(employees)

    # Створюємо словник індексів: ім'я -> номер рядка/стовпця
    index = {}
    for i in range(n):
        index[employees[i]] = i

    # Створюємо матрицю нулів розміром n x n
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)

    # Заповнюємо матрицю: ставимо 1 якщо є зв'язок
    for person in adjacency_list:
        for contact in adjacency_list[person]:
            i = index[person]
            j = index[contact]
            matrix[i][j] = 1

    return matrix


# --- Список ребер ---
def build_edge_list():
    edges = []

    for person in adjacency_list:
        for contact in adjacency_list[person]:
            # Сортуємо пару щоб уникнути дублів (Анна-Богдан і Богдан-Анна - одне ребро)
            if person < contact:
                edges.append((person, contact))

    return edges


# --- Головна програма ---

print("=" * 55)
print("АНАЛІЗ СОЦІАЛЬНОЇ МЕРЕЖІ КОМПАНІЇ")
print("=" * 55)


# 1. Список суміжності
print("\n1. СПИСОК СУМІЖНОСТІ:")
print("-" * 40)
for person in adjacency_list:
    contacts = ", ".join(adjacency_list[person])
    print(person + " -> " + contacts)


# 2. Матриця суміжності
matrix = build_adjacency_matrix()

print("\n2. МАТРИЦЯ СУМІЖНОСТІ:")
print("-" * 55)

# Друкуємо заголовок стовпців
header = " " * 12
for name in employees:
    header = header + name[:3] + " " * 5
print(header)

# Друкуємо рядки матриці
for i in range(len(employees)):
    row_str = employees[i] + " " * (12 - len(employees[i]))
    for j in range(len(employees)):
        row_str = row_str + str(matrix[i][j]) + " " * 7
    print(row_str)


# 3. Список ребер
edges = build_edge_list()

print("\n3. СПИСОК РЕБЕР (всього: " + str(len(edges)) + "):")
print("-" * 40)
for i in range(len(edges)):
    a = edges[i][0]
    b = edges[i][1]
    print(str(i + 1) + ". " + a + " - " + b)


# 4. Степені вершин
print("\n4. КІЛЬКІСТЬ ЗЯВЯЗКИВ КОЖНОГО СПИВРОБИТНИКА:")
print("-" * 40)

degrees = {}
for person in adjacency_list:
    degrees[person] = len(adjacency_list[person])

# Сортуємо від найбільшого до найменшого
sorted_employees = sorted(degrees, key=lambda x: degrees[x], reverse=True)

for person in sorted_employees:
    deg = degrees[person]
    print(person + ": " + str(deg) + " зв'язки")

most_social  = sorted_employees[0]
least_social = sorted_employees[-1]

print("\nНайбільш комунікабельний: " + most_social + " (" + str(degrees[most_social]) + " зв'язки)")
print("Найменш комунікабельний:  " + least_social + " (" + str(degrees[least_social]) + " зв'язки)")


# 5. Теорема про суму степенів
sum_degrees = 0
for person in degrees:
    sum_degrees = sum_degrees + degrees[person]

num_edges = len(edges)

print("\n5. ТЕОРЕМА ПРО СУМУ СТЕПЕНИВ:")
print("-" * 40)
print("Сума степенів всіх вершин: " + str(sum_degrees))
print("Кількість ребер: " + str(num_edges))
print("Подвоєна кількість ребер: " + str(2 * num_edges))

if sum_degrees == 2 * num_edges:
    print("Теорема підтверджена: " + str(sum_degrees) + " = 2 x " + str(num_edges))
else:
    print("Теорема не виконується!")

print("=" * 55)