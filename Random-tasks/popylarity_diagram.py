import matplotlib.pyplot as plt

# Данные для диаграммы в виде списка кортежей
orm_data = [
    ('SQLAlchemy', 35),
    ('Django ORM', 30),
    ('Tortoise ORM', 10),
    ('Peewee', 8),
    ('Pony ORM', 5),
    ('Orator', 4),
    ('GINO', 3),
    ('Beanie', 2),
    ('MongoEngine', 2),
    ('Pydal', 1)
]

# Разделение данных на два отдельных списка
orms, popularity = zip(*orm_data)

# Построение диаграммы
plt.figure(figsize=(10, 6))
plt.barh(orms, popularity, color='skyblue')
plt.xlabel('Популярность (%)')
plt.ylabel('ORM')
plt.title('Популярность Python ORM')
plt.gca().invert_yaxis()  # Инвертировать ось Y для отображения в порядке убывания
plt.show()