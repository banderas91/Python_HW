import random

def queens_are_safe(input):
    x = []
    y = []
    for i in range(8):
        a, b = map(int, input[i].split())
        x.append(a)
        y.append(b)
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def generate_positions():
    positions = []
    for i in range(8):
        row = random.randint(1, 8)
        col = random.randint(1, 8)
        positions.append(f"{row} {col}")
    return positions

def find_safe_positions():
    safe_positions = []
    attempts = 0
    while len(safe_positions) < 4:
        attempts += 1
        print(f"Попытка {attempts}...")
        positions = generate_positions()
        if queens_are_safe(positions):
            print("Найдена безопасная расстановка!")
            safe_positions.append(positions)
    return safe_positions

