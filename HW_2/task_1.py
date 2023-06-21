# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

hex_digits = '0123456789abcdef'
n = int(input('Введите целое число: '))
original_n = n
if n == 0:
    result = '0'
else:
    result = ''
    while n > 0:
        result = hex_digits[n % 16] + result
        n //= 16
print(result)

print(hex(int(result, 16)) == hex(original_n))
