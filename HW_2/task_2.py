# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions

first = int(input("Введите числитель первой дроби: "))
second = int(input("Введите знаменатель первой дроби: "))
third = int(input("Введите числитель второй дроби: "))
fourth = int(input("Введите знаменатель второй дроби: "))

result1 = (first / second) + (third / fourth)
result2 = (first / second) * (third / fourth)
print(result1)
print(result2)

first_fraction = fractions.Fraction(first, second)
second_fraction = fractions.Fraction(third, fourth)
result3 = first_fraction + second_fraction
result4 = first_fraction * second_fraction
print(result3)
print(result4)