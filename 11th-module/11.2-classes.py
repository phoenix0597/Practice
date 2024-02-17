# структурное программирование
# код с обработкой переменных с помощью условий, циклов...
user_name = "Admin"
password = "admin123"
is_banned = False


# объектно-ориентированное программирование
# работа с объектами класса с помощью его методов (ну и циклов, условий...)
class User:
    user_name = "Admin"
    password = "admin123"
    is_banned = False


user_1 = User()  # создание объекта - экземпляра класса User
user_2 = User()
user_2.user_name = "Alex"
print(user_1.user_name, user_2.user_name)

# если мы хотим изменить заданное по умолчанию имя пользователя,
# то надо обращаться не к экземпляру, а к самому классу
User.user_name = "Noname"
print(user_1.user_name, user_2.user_name)