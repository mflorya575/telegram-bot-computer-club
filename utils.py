import sqlite3


# Создаем подключение к базе данных (будет создан файл database.db)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


# Создаём функцию в которую передаём user_id, username, first_name
def add_user(user_id, username, first_name):
    # Получаем id пользователя из базы данных
    check_user = cursor.execute('SELECT * FROM Users WHERE id=?', (user_id,))

    # Проверяем есть ли пользователь уже в бд
    if check_user.fetchone() is None:
        # Добавляем пользователя
        cursor.execute(f"""INSERT INTO Users VALUES('{user_id}', '{username}', '{first_name}', 0); """)

    # Обновляем таблицу
    connection.commit()

# Функция вывода пользователей
def show_users():

    # Получаем все столбцы из таблицы в список users_list
    users_list = cursor.execute('SELECT * FROM Users')

    # Создаём переменную в которую будем записывать user_id, username, first_name пользователей
    message = ""

    # Проходимся по элементам списка и записываем их в переменную message
    for users in users_list:
        message += f"{users[0]} @{users[1]} {users[2]}\n"

    # Обновляем соединение с таблицей
    connection.commit()

    # Возвращаем переменную, которая будет служить сообщением для отправки при нажатии на кнопку
    return message

# Создаём функцию
def show_statistics():

    # Получаем список в котором записано количество элементов первого столбца таблицы
    count_users = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()

    # Обновляем соединение с таблицей
    connection.commit()

    # Возвращаем значение для отправки
    return count_users[0]

# Функция блокировки пользователей
def add_user_to_block(input_id):

    # Обновляем 0 на 1
    cursor.execute(f'UPDATE Users SET block = ? WHERE id = ?', (1, input_id))

    # Обновляем соединение с таблицей
    connection.commit()


# Функция для разблокировки пользователей
def unlock_users(input_id):
    # Обновляем 1 на 0
    cursor.execute(f'UPDATE Users SET block = ? WHERE id = ?', (0, input_id))

    # Обновляем соединение с таблицей
    connection.commit()


connection.commit()
connection.close()
