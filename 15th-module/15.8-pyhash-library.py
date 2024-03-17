# Библиотека pyhash
# Эта библиотека предоставляет широкий выбор хеш-функций, включая CRC, CityHash, FarmHash, SpookyHash и другие.
# Она обеспечивает гибкость выбора хеш-функции в зависимости от конкретных потребностей.
#
# Пример использования библиотеки pyhash для вычисления CRC32 хеш-значения строки:
import pyhash  # текущий релиз поддерживается до версии 3.10 (на дату 17.03.2024)

data = "Hello, World!"
crc32_hasher = pyhash.crc32()
hash_value = crc32_hasher(data)
print(hash_value)  # Выводит хеш-значение CRC32
