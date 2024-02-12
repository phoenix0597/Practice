# Task "Library" (2.1 Списки и их инициализация)
books_ID = [50, 34, -1, -1, 2, 23, -1]
new_books_ID = []
returned_num = 0

for _ in range(10):
	try:
		book_id = int(input("Введите ID книги: "))
	except ValueError:
		print("Вы ввели не число!")
		continue
	books_ID.append(book_id)

for book_id in books_ID:
	if book_id == -1:
		returned_num += 1
	else:
		new_books_ID.append(book_id)

print("\nВозвращено книг за день:", returned_num)
print("\nНовый список выданных книг:", new_books_ID)
