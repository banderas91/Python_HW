#  Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

lst = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 8, 8, 8]
duplicates = []
unique_elements = set()
for element in lst:
    if element in unique_elements:
        if element not in duplicates:
            duplicates.append(element)
    else:
        unique_elements.add(element)
print(f'Дублирующиеся элементы: {duplicates}')

