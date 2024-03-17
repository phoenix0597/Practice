class HashTable:
    def __init__(self):
        self.size = 10  # Размер хеш-таблицы
        self.table = [None] * self.size  # Инициализация массива с None
    
    def _hash_function(self, key):
        return hash(key) % self.size  # Хеш-функция, преобразующая ключ в индекс
    
    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index] = value  # Вставка значения по соответствующему индексу
    
    def get(self, key):
        index = self._hash_function(key)
        return self.table[index]  # Получение значения по ключу
    
    def remove(self, key):
        index = self._hash_function(key)
        self.table[index] = None  # Удаление значения по ключу


# Пример использования
hash_table = HashTable()
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

value = hash_table.get("key1")
print(value)  # Выводит "value1"

hash_table.remove("key2")
value = hash_table.get("key2")
print(value)  # Выводит None

print(hash_table.table)
print(hash_table._hash_function("key1"))
print(hash_table._hash_function("key2"))
print(hash_table._hash_function("key3"))

print(hash("key1"))
print([hash("key1")] * 5)
print(hash_table.size)