import sqlite3

"""
Д.З. 14_1 / 14_2
"""
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

"""
Создайте таблицу Users, если она ещё не создана.
"""
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS 
    Users 
    (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')

"""
Заполните таблицу 10 записями:
"""
for num in range(1, 11):
    cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
        (f'User{num}', f'example{num}@gmail.com', f'{num * 10}', '1000')
    )

"""
Обновите balance у каждой 2ой записи начиная с 1ой на 500:
"""
for num in range(1, 11, 2):
    cursor.execute(
        "UPDATE Users SET balance = ? WHERE username = ?",
        (f'500', f'User{num}',)
    )

"""
Удалите каждую 3ую запись в таблице начиная с 1ой:
"""
for num in range(1, 11, 3):
    cursor.execute(
        "DELETE FROM Users WHERE username = ?",
        (f'User{num}',)
    )

"""
Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60
"""
cursor.execute(
    "SELECT username, email, age, balance FROM Users WHERE age != ?",
    (60,)
)

"""
выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
"""
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
#
#
""" 
Д./З. 14_2 
Выбор элементов и функции в SQL запросах
"""
#

"""
Удалите из базы данных not_telegram.db запись с id = 6.
"""
cursor.execute(
    "DELETE FROM Users WHERE id = ?",
    (f'{6}',)
)

"""
Подсчитать общее количество записей.
"""
cursor.execute("SELECT COUNT(*) FROM Users")
count_users = cursor.fetchone()[0]

"""
Посчитать сумму всех балансов.
"""
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]

"""
Вывести в консоль средний баланс всех пользователей.
"""
print(sum_balance / count_users)

# Можно закомментировать
""" Удаляет каждую запись в таблице. """
for num in range(1, 11):
    cursor.execute(
        "DELETE FROM Users WHERE username = ?",
        (f'User{num}',)
    )

connection.commit()
connection.close()
