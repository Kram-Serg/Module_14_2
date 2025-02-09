import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# i = 0
# for j in range(10, 101, 10):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                     (f'User{i+1}', f'example{i+1}@gmail.com', j, '1000'))
#     i += 1
#
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?',(f'{i}',))
#
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
# users = cursor.fetchall()
#
# for user in users:
#     print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} |  Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]

print(all_balance/total_users)

connection.commit()
connection.close()
