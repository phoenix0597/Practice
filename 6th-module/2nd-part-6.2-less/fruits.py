# Задача 2. Кризис фруктов
# Мы работаем в одной небольшой торговой компании, где все данные о продажах фруктов за год сохранены в словаре
# в виде пар «название фрукта — доход»:
#
# В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.
# Напишите программу, которая находит общий доход, затем выводит фрукт с минимальным доходом и удаляет его из словаря.
# Выведите итоговый словарь на экран.
#
# Результат работы программы:
# Общий доход за год составил 35419.34 рублей
# Самый маленький доход у grapefruit. Он составляет 300.4 рублей
# Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0, 'bergamot': 3700.56,
# 'durian': 5987.23, 'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total_income = sum(incomes.values())
print('Общий доход за год составил', round(total_income, 2), 'рублей')

min_income_val = min(incomes.values())
# определяем ключ с минимальным значением
min_income_key = min(incomes, key=incomes.get)
print(f"Самый маленький доход у {min_income_key}. Он составляет {round(min_income_val, 2)} рублей")

incomes.pop(min_income_key)
print("Итоговый список фруктов:\n", incomes)
