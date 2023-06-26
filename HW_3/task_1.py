# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends = {
    'Андрей': ('палатка', 'спальник', 'фонарик'),
    'Сергей': ('спальник', 'фонарик', 'кастрюля'),
    'Иван': ('палатка', 'спальник', 'фонарик', 'лопата')
}

all_items = set(friends['Андрей'])
for friend in friends:
    all_items = all_items.intersection(friends[friend])
print(f'Вещи, которые взяли все три друга: {all_items}')

unique_items = set()
for friend in friends:
    unique_items = unique_items.symmetric_difference(friends[friend])
print(f'Уникальные вещи: {unique_items}')

for friend in friends:
    other_friends = set(friends.keys()) - {friend}
    other_items = set()
    for other_friend in other_friends:
        other_items = other_items.union(friends[other_friend])
    missing_items = other_items - set(friends[friend])
    if missing_items:
        print(f'У {friend} отсутствуют следующие вещи: {missing_items}')
