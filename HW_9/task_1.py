# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import random
from typing import List, Tuple

def quadratic_roots(a: float, b: float, c: float) -> Tuple[float, float]:
    """Нахождение корней квадратного уравнения"""
    d = b**2 - 4*a*c
    if d < 0:
        raise ValueError("Уравнение не имеет действительных корней")
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    return x1, x2

def generate_csv(filename: str, rows: int = 1000):
    """Генерация csv файла с тремя случайными числами в каждой строке"""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(rows):
            row = [random.random() for _ in range(3)]
            writer.writerow(row)

def from_csv(decorated):
    """Декоратор, запускающий функцию с каждой тройкой чисел из csv файла"""
    def wrapper(filename: str):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(float, row)
                decorated(a, b, c)
    return wrapper

def to_json(decorated):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл"""
    def wrapper(*args, filename: str = 'output.json'):
        result = decorated(*args)
        data = {
            'args': args,
            'result': result
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        return result
    return wrapper

@to_json
@from_csv
def solve_quadratic_from_csv(a: float, b: float, c: float):
    """Нахождение корней квадратного уравнения для каждой тройки чисел из csv файла"""
    return quadratic_roots(a, b, c)


generate_csv('data.csv', rows=100)
solve_quadratic_from_csv('data.csv', filename='output.json')


