import sqlite3 as sl

con = sl.connect('my-test.db')

#Создание таблицы
#with con:
#    con.execute("""
#        CREATE TABLE SCHOOL (
#            id       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            name     TEXT,
#            algebra  INTEGER,
#            physics  INTEGER,
#            russian  INTEGER,
#            class    TEXT
#        );
#    """)

#Подготовка данных
#sql = 'INSERT INTO SCHOOL (id, name, algebra, physics, russian, class) values(?, ?, ?, ?, ?, ?)'
#data = [
#    (1, 'Ivanov',     3, 2, 2, '10a'),
#    (2, 'Petrov',     4, 4, 5, '10b'),
#    (3, 'Iablochkin', 5, 4, 5, '10a'),
#    (4, 'Grushin',    5, 5, 5, '10b'),
#    (5, 'Lastochkin', 4, 3, 2, '10v')
#]

#Исполнить
#with con:
#    con.executemany(sql, data)

#Выбираем данные согласно заданию
print("Список всех хорошистов")
with con:
    data = con.execute("SELECT * FROM SCHOOL where algebra >= 4 and physics >= 4 and russian >= 4")
    for row in data:
        print(row)

print("\r\nОдна двойка")
with con:
    data = con.execute("SELECT * FROM SCHOOL where (algebra = 2 and physics <> 2 and russian <> 2) or (physics = 2 and algebra <> 2 and russian <> 2) or (russian = 2 and algebra <> 2 and physics <> 2)")
    for row in data:
        print(row)

print("\r\nКласс в котором больше всего хорошистов")
with con:
    data = con.execute("SELECT class, count(class) as cnt FROM SCHOOL where algebra = 4 or physics = 4 or russian = 4 group by class HAVING max(class)")
    for row in data:
        print(row)

print("\r\nКласс в котором больше всего школьников получили 5 по алгебре")
with con:
    data = con.execute("SELECT class, count(algebra) as cnt FROM SCHOOL where algebra = 5 group by class HAVING max(algebra)")
    for row in data:
        print(row)