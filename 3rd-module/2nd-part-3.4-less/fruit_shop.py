# 3.4. Магазин фруктов
# В небольшой фруктовой лавке у каждого фрукта есть название и цена.
# Эта информация хранится в одном большом списке, вот так:
# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
# Недавно в лавку привезли новый fruit_name по цене price, а после этого случилось ужасное: повысили налоги.
# А значит, повысились и цены на фрукты, на целых 8%!
# Реализуйте код, который добавляет в список goods ещё один список с новым фруктом и ценой
# (это запрашивается у пользователя), а затем увеличивает цены всех фруктов на 8%.
goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print("\nТекущий ассортимент: ", goods)
nem_fruit_name = input("Введите название нового фрукта: ")
new_fruit_price = int(input("Введите цену нового фрукта: "))

goods.append([nem_fruit_name, new_fruit_price])
print("Новый ассортимент: ", goods)

extra_charge = int(input("Введите процент повышения цен: "))
for i_num in range(len(goods)):
	goods[i_num][1] = round(goods[i_num][1] * (1 + extra_charge / 100), 2)
print("Новый ассортимент: ", goods)
