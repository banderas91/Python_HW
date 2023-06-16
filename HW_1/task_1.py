title = 'ТАБЛИЦА УМНОЖЕНИЯ'
print(f'{title:^55}\n')
for i in range(2, 11):
    for j in range(2, 6):
        if i == 10:
            print(f'{j} x {i} ={i*j}', end='\t')
        else:
            print(f'{j} x {i} = {i*j}', end='\t')
    print()
print()
for i in range(2, 11):
    for j in range(6, 10):
        if i == 10:
            print(f'{j} x {i} ={i*j}', end='\t')
        else:
            print(f'{j} x {i} = {i*j}', end='\t')
    print()
