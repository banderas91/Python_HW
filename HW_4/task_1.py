# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. 
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

a = 1
b = 2
c = 3
ds = 4
es = 5
s = 6

def replace_s(globals_dict):
    for key, value in list(globals_dict.items()):
        if key.endswith('s') and key != 's':
            new_key = key[:-1]
            globals_dict[new_key] = value
            globals_dict[key] = None

replace_s(globals())

print(a) 
print(b) 
print(c) 
print(ds) 
print(es) 
print(d) 
print(e) 
print(s)