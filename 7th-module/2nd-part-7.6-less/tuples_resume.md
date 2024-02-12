### Итоги 7-го модуля
1. Если нужно защитить данные от каких-то изменений, то можно использовать кортежи
    nums = (1, 2, 3)
    nums = tuple(nums_list)
Кортежи легче и быстрее, чем списки.
2. Из функции может возвращаться несколько значений. В таком случае они возвращают кортеж из этих значений, 
которые можно разложить на отдельные переменные. 

    user = get_user() # ('Bob', 'Ivanov', 45)
    name, surname, age = get_user()
3. Если нам нужно в цикле отслеживать индекс элемента и его значение, то для этого используются две переменные 
и функция enumerate

    for index, value in enumerate(nums):

4. При такой же работе со словарем используется метод items(), который возвращает отображение кортежей

    for key, value in new_dict.items():

5. В качестве ключа словаря можно использовать кортеж из элементов. Это называется составным ключом

    phonebook_dict = {
        ('Ivan', 'Ivanov'): 1234567890,
        ('Petr', 'Petrov'): 9876543210
    }

6. Если нам попарно нужно объединить элементы двух списков в один общий список или словарь, то для этого 
можно использовать функцию zip()

    names = ['John', 'Corey', 'Adam']
    ages = [45, 40, 35]
    people = zip(names, ages)
    print(list(people))
7. Использование генераторов экономит память и делает приложение более быстрым и легковесным (Pythonic way):
    # эта функция возвращает генератор
    def my_zip(coll_1, coll_2):
        return ((coll_1[i], coll_2[i]) for i in range(min(len(coll_1), len(coll_2))))

    # тестирование работы программы
    test_string_1 = 'abcd'
    test_tuple_1 = (10, 20, 30, 40)
    print('\nРабота аналога функции zip():')
    
    # этот print() выводит следующее: <generator object my_zip.<locals>.<genexpr> at 0x000001FEF2D91700>
    print(my_zip(test_string_1, test_tuple_1))  
    
    