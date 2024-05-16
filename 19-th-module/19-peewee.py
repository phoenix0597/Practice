from peewee import SqliteDatabase, Model, CharField, IntegerField

# подключаемся к базе данных my_database.db
db = SqliteDatabase("my_database.db")


# создаём модель User
class User(Model):
    # имя пользователя, CharField -- строка
    name = CharField()
    # возраст пользователя, IntegerField -- целое число
    age = IntegerField()
    
    # во внутреннем классе Meta указываем нашу базу данных
    
    class Meta:
        database = db


# # создаём таблицу users в базе данных
db.create_tables([User])

# Добавим пользователей в базу данных
user1 = User(name="Дима", age=25)
user1.save()
user2 = User(name="Костя", age=30)
user2.save()

# Выведем пользователей
users = User.select()  # получаем список пользователей
for user in users:
    print(user.name, user.age)
# Дима 25
# Костя 30

# # Для получения объекта из базы используется метод .get с перечислением критериев поиска:
# retrieved_user = User.get(User.name == "Дима")
# #
# # Изменить модель так же просто, как и создать её:
# retrieved_user.name = "Дмитрий"
# retrieved_user.save()
#
# # Удалить модель можно с помощью метода .delete_instance:
# user2.delete_instance()

# To delete all users with the name "Дмитрий" from the database, you can use the delete method provided by Peewee.
# Here's the code:
User.delete().where(User.name == "Костя").execute()
