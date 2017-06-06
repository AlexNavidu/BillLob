import csv
from test_csv import villains
with open('villains', 'rt') as fin: # менеджер контекста.
    cin = csv.reader(fin)
    villains = [row for row in cin] # Здесь используется включение списка

print(villains)
