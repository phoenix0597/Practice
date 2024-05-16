import sqlite3

with sqlite3.connect("database.db") as conn:
    # Чтобы использовать SQL и получать результаты запросов, нужен курсор - спец. объект, создаваемый методом cursor()
    cursor = conn.cursor()
    # Метод .execute исполняет переданный SQL-запрос
    cursor.execute("SELECT * FROM students")
    # С помощью fetchall() мы можем получить все записи, который этот запрос нам вернул, в виде списка кортежей
    print(cursor.fetchall())
    
    
    # Важно! После добавления, изменения или удаления записей необходимо с помощью метода commit() у объекта Connection
    # зафиксировать изменения, внесенные в базу данных
    conn.commit()
    