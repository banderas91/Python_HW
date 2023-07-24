# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку
import csv
import pickle

with open('res.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    data = [dict(zip(headers, row)) for row in reader]

print(pickle.dumps(data))
