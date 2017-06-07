import sqlite3

conn = sqlite3.connect('enterprise.db')
# создание объекта курсора, для взаимодействия с БД.
curs = conn.cursor()
# execute - запуск команды SQL.
curs.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages INT)''')

# добавляем в базу данных айтемы.
сurs.execute('INSERT INTO zoo VALUES("duck", 5, 0)')
сurs.execute('INSERT INTO zoo VALUES("bear", 2, 1000)')
# используем для примера заполнитель.
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)'
curs.execute(ins, ('weasel', 1, 2000))

curs.execute('SELECT * FROM zoo')

curs.close()
conn.close()
