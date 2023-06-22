'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака.'''
items = {
    'тент': 3,
    'спальный мешок': 2,
    'фонарик': 1,
    'еда': 4,
    'вода': 5
}

backpack_capacity = 10
possible_combinations = [[]]

for item, weight in items.items():
    new_combinations = []
    for combination in possible_combinations:
        new_combination = combination + [(item, weight)]
        total_weight = sum(w for _, w in new_combination)
        if total_weight <= backpack_capacity:
            new_combinations.append(new_combination)
    possible_combinations.extend(new_combinations)

valid_combinations = [combination for combination in possible_combinations if sum(w for _, w in combination) <= backpack_capacity]

print("Все возможные варианты комплектации рюкзака:")
for combination in valid_combinations:
    print("Вещи:", [item[0] for item in combination])
    print("Общая масса:", sum(item[1] for item in combination))
    print()
