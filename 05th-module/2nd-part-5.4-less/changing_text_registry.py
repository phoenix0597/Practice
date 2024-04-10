def upper_more_than_lower(text):
	up_reg_count = 0
	low_reg_count = 0
	for char in text:
		if char.isupper():
			up_reg_count += 1
		if char.islower():
			low_reg_count += 1
	return up_reg_count >= low_reg_count


print("Введите текст: ", end="")
input_text = input()
if upper_more_than_lower(input_text):
	output_text = input_text.upper()
else:
	output_text = input_text.lower()

print("Результат: ", output_text)
